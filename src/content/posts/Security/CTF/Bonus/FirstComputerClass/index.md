---
title: "[CTF] 2DArray"
published: 2024-08-01
description: 감사합니다!
image: ""
tags: [hacking]
category: Security
draft: true
---



```py
import socket

def set_bit(value, position):
    return value | (1 << position)

def clear_bit(value, position):
    return value & ~(1 << position)

def parse_problem(problem_str):
    print(problem_str)
    def split_g(string):
        result = []
        current = ""

        space = False

        for i in string:
            if i == '}':
                space = True
                current+=i
            elif space:
                space = False
                result.append(current)
                current=""
            else:
                current += i
        result.append(current)
        return result
    parts = split_g(problem_str)
    binary_str = parts[0][1:-1]
    print(binary_str, parts[1])
    set_positions = set(list(map(int, parts[1][1:-1].split(':')[1].split())))
    print(1, set_positions)
    clear_positions = set(list(map(int, parts[2][1:-1].split(':')[1].split())))
    print(set_positions, clear_positions)
    # set_positions = [int(pos) for pos in parts[1].split() if pos]
    # clear_positions = [int(pos) for pos in parts[2].split(',') if pos]
    value = int(binary_str, 2)
    return value, set_positions, clear_positions

def solve_problem(value, set_positions, clear_positions):
    for pos in set_positions:
        value = set_bit(value, pos)
    for pos in clear_positions:
        value = clear_bit(value, pos)
    return value

def start_client():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        try:
            problem_str = s.recv(1024).decode()
            print("Received problem from server:", problem_str)
            value, set_positions, clear_positions = parse_problem(problem_str)
            solution = solve_problem(value, set_positions, clear_positions)
            print("Sending solution to server:", f"{solution:07b}")
            s.sendall(str(solution).encode())
            response = s.recv(1024).decode()
            print('Server response:', response)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_client()
```
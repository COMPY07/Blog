---
title: "[BOJ] N-Queen"
published: 2024-07-08
description: 너무나 유명한 문제 N퀸!!
image: ""
tags: [algorithm, ps]
category: CS
draft: false
---

[N-Queen](https://www.acmicpc.net/problem/9663)

| TimeLimit | MemoryLimit |   Condition   |           TAG      |
|:---------:|:-----------:|:-------------:|:------------------:|
|    10s    |    128MB    | (1<= N <= 15) | BackTracking(백트래킹) |

> N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
>
> N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.


일단 이 문제는 정말 단순한 구현문제이다. 그냥 완전탐색에 가지치기 몇 번하면 그냥 풀리는 문제이니 사실 어려움은 없을 것이다.
물론 구현이 가능하면 말이다.

퀸이 이동 가능한 위치를 알고서, 가로 세로 대각선을 체크만 한다면 너무나 쉬운 문제라 딱히 해설을 하지 않겠다.

(지금 다른 포스팅을 하고있는데 쓸 포스팅이 고갈되어서 이거 씁니다... ㅠㅜㅜ)<br>
(혹시라도 궁금하시면 아래 코드 함 보시고 생각해보시길.. 별로 좋은 코드는 아닌거 같아여)

<details>
<summary> 정답 코드 </summary>

```cpp
#include <iostream>
bool IsSafe(int y, int x, bool arr[15][15], int N, bool* row);
int solution(int n, bool board[15][15], int current, bool* row);
using namespace std;



int result;



int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int n;
    bool board[15][15] = {false, };
    bool row[15] = {false,};
    
    cin >> n;
    
    cout << solution(n, board, 0, row);
    
}
void printBoard(bool board[15][15], int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << board[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}
int solution(int n, bool board[15][15], int current, bool* row){
    if(current == n) return 1;
    
    int mysum = 0;
    
    for(int i = 0; i < n; i++){
        if(!IsSafe(current, i, board, n, row)) continue;
        board[current][i] = true;
        row[i] = true;
        mysum += solution(n, board, current+1, row);
        board[current][i] = false;
        row[i] = false;
    }
    return mysum;
    
}

bool IsSafe(int y, int x, bool arr[15][15], int N, bool* row){
    if(row[x]) return false;
    
    
    for(int i = 1; i < N; i++){
        if(0 <= y+i && y+i < N && 0 <= x+i && x+i < N && arr[y+i][x+i]) return false;
        if(0 <= y-i && y - i < N && 0 <= x-i && x-i < N && arr[y-i][x-i]) return false;
        if(0 <= y+i && y+i < N && 0 <= x-i && x-i < N && arr[y+i][x-i]) return false;
        if(0 <= y-i && y - i < N && 0 <= x+i && x+i < N && arr[y-i][x+i]) return false;
    }
    
    return true;
}

```

</details>

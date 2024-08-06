---
title: "[Reversing] DreamHack Basic revs"
published: 2024-08-05
description: basic rev 모든 풀이
image: ""
tags: [hacking, rev]
category: Security
draft: false
---

사실 rev 3까지는 눈을 풀이가 가능하긴 합니다.
2까진 진짜 눈으로만 풀 수 있고요, 3부터는 좀 편하게 풀기 위해서 코드를 작성합니다.




## basic rev 3

그냥 한번 뜯어보면 아시다 싶이 그냥 같기만 하면 되기에 그대로 출력합니다. - _ 이거 잘 구분하셔요!
```py
answer = [0x49, 0x60, 0x67, 0x74, 0x63, 0x67, 0x42, 0x66, 0x80, 0x78,
          0x69, 0x69, 0x7B, 0x99, 0x6D, 0x88, 0x68, 0x94, 0x9F, 0x8D, 0x4D, 0xA5, 0x9D, 0x45, 0x00]

answer = [answer[i] - 2 * i for i in range(0x18)]
answer = [answer[i] ^ i for i in range(0x18)]
print(*[chr(i) for i in answer], sep="")
```

<br><br><br><br><br>

## basic rev 4

이 문제는 조금 생각을 하면 금방 풀 수 있습니다. 먼저 char가 1byte라는 사실만 안다면 어렵지 않게 풀 수 있어요.
*2하는 것은 shift 연산으로 표현하자면 << 1이에요. -> a << 4 | a >> 4이게 되죵.
char는 1byte = 8bit 즉 기본 값에성 << 4가 되면 하위 비트, >> 4가 되면 상위 비트이런 식으로 생각이 가능하죠
```py
answer = [0x24, 0x27, 0x13, 0xc6, 0xc6, 0x13, 0x16, 0xe6, 0x47, 0xf5, 0x26, 0x96, 0x47, 0xf5, 0x46, 0x27, 0x13, 0x26, 0x26, 0xc6, 0x56, 0xf5, 0xc3, 0xc3, 0xf5, 0xe3, 0xe3, 0x00]
 
for i in answer:
    if i == 0x00: break
    hex_value = str(hex(i))[2:]

    print(chr(int(hex_value[0], 16)
          + int(hex_value[1]+'0', 16)), end="")
```

<br><br><br><br><br>


## basic rev 5

이번 문제는 그냥 빼는 문제라 딱히 생각이 필요하지 않습니다.
```py
answer = [0xad, 0xd8, 0xcb, 0xcb, 0x9d, 0x97, 0xcb, 0xc4, 0x92, 0xa1, 0xd2, 0xd7, 0xd2, 0xd6, 0xa8, 0xa5, 0xdc, 0xc7, 0xad, 0xa3, 0xa1, 0x98, 0x4c, 0x00]
#
# print(len(answer), 0x18)
for i in range(0x18-2, -1, -1):
    answer[i]-=answer[i+1]

for i in range(0x18):
    print(chr(answer[i]), end='')
```

<br><br><br><br><br>


## basic rev 6

이것도 그냥 위치 찾아서 반환하면 되는 문제라 딱히 생각이 필요 없습니다.
```py
answer = [0x00, 0x4d, 0x51, 0x50, 0xef, 0xfb, 0xc3, 0xcf, 0x92, 0x45, 0x4d, 0xcf, 0xf5, 0x04, 0x40, 0x50, 0x43, 0x63, 0x00]

string_list = list(map(lambda x: int(x, 16), """63 7C 77 7B F2 6B 6F C5  30 01 67 2B FE D7 AB 76
 CA 82 C9 7D FA 59 47 F0  AD D4 A2 AF 9C A4 72 C0
 B7 FD 93 26 36 3F F7 CC  34 A5 E5 F1 71 D8 31 15
 04 C7 23 C3 18 96 05 9A  07 12 80 E2 EB 27 B2 75
 09 83 2C 1A 1B 6E 5A A0  52 3B D6 B3 29 E3 2F 84
 53 D1 00 ED 20 FC B1 5B  6A CB BE 39 4A 4C 58 CF
 D0 EF AA FB 43 4D 33 85  45 F9 02 7F 50 3C 9F A8
 51 A3 40 8F 92 9D 38 F5  BC B6 DA 21 10 FF F3 D2
 CD 0C 13 EC 5F 97 44 17  C4 A7 7E 3D 64 5D 19 73
 60 81 4F DC 22 2A 90 88  46 EE B8 14 DE 5E 0B DB
 E0 32 3A 0A 49 06 24 5C  C2 D3 AC 62 91 95 E4 79
 E7 C8 37 6D 8D D5 4E A9  6C 56 F4 EA 65 7A AE 08
 BA 78 25 2E 1C A6 B4 C6  E8 DD 74 1F 4B BD 8B 8A
 70 3E B5 66 48 03 F6 0E  61 35 57 B9 86 C1 1D 9E
 E1 F8 98 11 69 D9 8E 94  9B 1E 87 E9 CE 55 28 DF
 8C A1 89 0D BF E6 42 68  41 99 2D 0F B0 54 BB 16""".split()))

for i in range(0x12):
    print(chr(string_list.index(answer[i])), end="")
```

<br><br><br><br><br>



## basic rev 7

이번 문제는 그냥 circular shift 구현만 할 수 있으면 그냥 풀리는 문제라 이번 또한 딱히 생각할 필요는 없습니다.
```py

def rol_left(max_bit, rotate_bit, count):
    max_bit = 1 << (max_bit-1)
    check = False
    for i in range(count):
        if rotate_bit & max_bit: check = True
        rotate_bit <<= 1

        if check: rotate_bit+=1
        check = False
    return rotate_bit

def rol_right(max_bit, rotate_bit, count):
    max_bit = 1 << (max_bit-1)
    check = False
    for i in range(count):
        if rotate_bit & 1: check = True
        rotate_bit >>= 1

        if check: rotate_bit+=max_bit
        check = False
    return rotate_bit
print(roc_right(8, 7, 1))

answer = list(map(lambda x : int(x, 16), """52 DF B3 60 F1 8B 1C B5  57 D1 9F 38 4B 29 D9 26
7F C9 A3 E9 53 18 4F B8  6A CB 87 58 5B 39 1E 00""".split()))
for i in range(0x1f):
    print(chr(rol_right(8, answer[i]^i, i & 7)), end="")

# ROL1 는 LCIRC랑 똑같다고 생각하심 됩니다.
```

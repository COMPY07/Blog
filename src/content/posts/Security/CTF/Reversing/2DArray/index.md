---
title: "[CTF] 2DArray"
published: 2024-08-01
description: 그냥 역산
image: ""
tags: [hacking, rev]
category: Security
draft: true
---

```c

bool FUN_001016ba(void)

{
  int iVar1;
  long in_FS_OFFSET;
  uint local_60;
  uint local_5c;
  undefined local_58 [72];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  setvbuf(stdout,(char *)0x0,2,0);
  memset(local_58,0,0x40);
  for (local_5c = 0; (int)local_5c < 8; local_5c = local_5c + 1) {
    for (local_60 = 0; (int)local_60 < 8; local_60 = local_60 + 1) {
      printf("value of (%d, %d)? ",(ulong)local_60,(ulong)local_5c);
      __isoc99_scanf(&DAT_00102032,local_58 + (long)(int)local_5c * 8 + (long)(int)local_60);
    }
  }
  FUN_0010133f(local_58);
  FUN_0010158a(local_58,&DAT_00102037,8);
  FUN_00101407(local_58);
  FUN_00101622(local_58,&DAT_00102040,8);
  FUN_001014d0(local_58);
  iVar1 = memcmp(local_58,&DAT_00102050,0x40);
  if (iVar1 != 0) {
    puts("wrong :(");
  }
  else {
    printf("correct :) flag is ");
    FUN_00101289();
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return iVar1 != 0;
}

```
<details>


FUN_0010133f
```c

void FUN_0010133f(long param_1)

{
  undefined uVar1;
  int local_10;
  int local_c;
  
  for (local_c = 0; local_c < 4; local_c = local_c + 1) {
    for (local_10 = 0; local_10 < 8; local_10 = local_10 + 1) {
      uVar1 = *(undefined *)((long)local_c * 8 + param_1 + (long)local_10);
      *(undefined *)((long)local_c * 8 + param_1 + (long)local_10) =
           *(undefined *)((long)(8 - local_c) * 8 + -8 + param_1 + (long)local_10);
      *(undefined *)((long)(8 - local_c) * 8 + -8 + param_1 + (long)local_10) = uVar1;
    }
  }
  return;
}

```

<br>

FUN_0010158a
```c

void FUN_0010158a(long param_1,long param_2,ulong param_3)

{
  int local_10;
  int local_c;
  
  for (local_c = 0; local_c < 8; local_c = local_c + 1) {
    for (local_10 = 0; local_10 < 8; local_10 = local_10 + 1) {
      *(byte *)((long)local_c * 8 + param_1 + (long)local_10) =
           *(byte *)((long)local_c * 8 + param_1 + (long)local_10) ^
           *(byte *)(param_2 + (ulong)(long)(local_c + local_10) % param_3);
    }
  }
  return;
}

```

<br>

FUN_00101407
```c

void FUN_00101407(long param_1)

{
  undefined uVar1;
  int local_10;
  int local_c;
  
  for (local_c = 0; local_c < 8; local_c = local_c + 1) {
    for (local_10 = 0; local_10 < 4; local_10 = local_10 + 1) {
      uVar1 = *(undefined *)((long)local_c * 8 + param_1 + (long)local_10);
      *(undefined *)(param_1 + (long)local_c * 8 + (long)local_10) =
           *(undefined *)((long)local_c * 8 + param_1 + (long)(7 - local_10));
      *(undefined *)((long)local_c * 8 + param_1 + (long)(7 - local_10)) = uVar1;
    }
  }
  return;
}


```


<br>


FUN_00101622
```c

void FUN_00101622(long param_1,long param_2,ulong param_3)

{
  int local_10;
  int local_c;
  
  for (local_c = 0; local_c < 8; local_c = local_c + 1) {
    for (local_10 = 0; local_10 < 8; local_10 = local_10 + 1) {
      *(char *)((long)local_c * 8 + param_1 + (long)local_10) =
           *(char *)((long)local_c * 8 + param_1 + (long)local_10) +
           *(char *)(param_2 + (ulong)(long)(local_c + local_10) % param_3);
    }
  }
  return;
}


```


<br>

FUN_001014d0
```c

void FUN_001014d0(long param_1)

{
  undefined uVar1;
  int local_10;
  int local_c;
  
  for (local_c = 0; local_c < 8; local_c = local_c + 1) {
    for (local_10 = local_c; local_10 < 8; local_10 = local_10 + 1) {
      uVar1 = *(undefined *)((long)local_c * 8 + param_1 + (long)local_10);
      *(undefined *)((long)local_c * 8 + param_1 + (long)local_10) =
           *(undefined *)((long)local_10 * 8 + param_1 + (long)local_c);
      *(undefined *)((long)local_10 * 8 + param_1 + (long)local_c) = uVar1;
    }
  }
  return;
}


```

</details>

<br>

그냥 역산 한거라 딱히 설명할게 없는데...



```py
board = [
    [0x19, 0xdf, 0xf7, 0xfd, 0xc0, 0xae, 0x9b, 0xc8],
    [0xe4, 0x5d, 0x06, 0xf5, 0x1d, 0x71, 0x0e, 0xee],
    [0xc0, 0x1c, 0x3e, 0x14, 0x33, 0x32, 0x40, 0x69],
    [0x35, 0x68, 0x02, 0xe2, 0xb7, 0x20, 0x1f, 0x3d],
    [0xf5, 0x19, 0x57, 0xd2, 0x97, 0xdd, 0x30, 0x90],
    [0x43, 0xbc, 0x7b, 0xa8, 0x15, 0x89, 0xbd, 0x53],
    [0x40, 0xcf, 0x64, 0x3d, 0x8d, 0x03, 0xae, 0x2e],
    [0x08, 0x5a, 0xae, 0x9a, 0x11, 0x9f, 0xb7, 0x65]
]

def cross_value_x(board):
    # board 걍 2차원으로 가보자
    for i in range(8):
        for j in range(i, 8):
            tmp = board[i][j]
            board[i][j] = board[j][i]
            board[j][i] = tmp
    return board


board = cross_value_x(board)



def xor_cross_1(board):
    data = [0xbf, 0xd6, 0x62, 0x87, 0x08, 0x62, 0xf2, 0x66]
    for i in range(8):
        for j in range(8):
            board[i][j] -= data[(i+j)%8]
    return board
board = xor_cross_1(board)

def cross_value_x_1(board):
    for i in range(8):
        for j in range(4):
            tmp = board[i][j]
            board[i][j] = board[i][7-j]
            board[i][7-j] = tmp
    return board

board= cross_value_x_1(board)

def xor_cross_2(board):
    data = [0x15, 0x55, 0xc4, 0x3b, 0xb5, 0xfc, 0x35, 0xd7]
    for i in range(8):
        for j in range(8):
            board[i][j] ^= data[(i+j)%8]
    return board

board = xor_cross_2(board)

def cross_value_y_1(board):
    for i in range(4):
        for j in range(8):
            tmp = board[i][j]
            y = (8-i)*8-8+j
            board[i][j] = board[y//8][y%8]
            board[y//8][y%8] = tmp
    return board

board = cross_value_y_1(board)

from pwn import *

p = remote("srv1.kitriwhs.kr", 18281)
for i in range(8):
    for j in range(8):
        p.sendlineafter(f"value of ({j}, {i})? ", str(board[i][j]))

p.interactive()
```
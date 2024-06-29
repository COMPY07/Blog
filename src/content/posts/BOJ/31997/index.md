---
title: "[BOJ] 즐거운 회의"
published: 2024-06-29
description: 31997 풀이
image: ""
tags: [ps, algorithm]
category: CS
draft: false
---

[즐거운 회의](https://www.acmicpc.net/problem/31997)

> 1번부터 N번까지 N명의 사람들이 시각 t=0에서 t=T까지 진행되는 회의에 참석한다. 
> i번 사람은 시각 t=a_i에 와서 t=b_i에 떠난다. 서로 다른 A번 사람과 B번 사람이 서로 친하면 두 사람이 회의에 참석하는 동안 즐거운 대화를 나눌 수 있다.
>
> 사람들이 회의를 오고 떠나는 시각과 어떤 사람들이 서로 친한지 주어진다. 각 시각 t=0.5, t=1.5, ..., t=T-0.5에 즐거운 대화를 나누고 있는 사람들이 총 몇 쌍 있는지 구하여라.
>
> 사람들의 쌍을 셀 때, 순서는 고려하지 않는다. 즉, A번 사람과 B번 사람의 쌍은 B번 사람과 A번 사람의 쌍과 같다.

문제가 굉장히 간단하기 때문에 그냥 바로 풀어버렸다.

코드를 보면 바로 이해할 수 있다.

그냥 현재의 시간과 다음 시간 조건만 확인하면 풀이를 할 수 있다.
(정말 간단한 로직으로 풀이가 가능하다.)

```py
result = [0] * (t+1)
timetable = {i: () for i in range(n + 1)}

for i in range(n):
    a, b = map(int, input().split())
    limit = b - a
    timetable[i] = (a, b)

for i in range(m):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    if timetable[b][0] > timetable[a][1] or timetable[a][0] > timetable[b][1]: continue

    if timetable[a][0] > timetable[b][0]: result[timetable[a][0]]+=1
    else: result[timetable[b][0]] += 1

    result[min(timetable[a][1], timetable[b][1])] -= 1

```

이렇게 단 한번의 루프로 다 돌릴 수 있다.

<details>
<summary> 정답 코드 </summary>

```py
n, m, t = map(int, input().split())
result = [0] * (t+1)
timetable = {i: () for i in range(n + 1)}

for i in range(n):
    a, b = map(int, input().split())
    limit = b - a
    timetable[i] = (a, b)

for i in range(m):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    if timetable[b][0] > timetable[a][1] or timetable[a][0] > timetable[b][1]: continue

    if timetable[a][0] > timetable[b][0]: result[timetable[a][0]]+=1
    else: result[timetable[b][0]] += 1

    result[min(timetable[a][1], timetable[b][1])] -= 1


current = 0
for i in range(t):
    current+=result[i]
    print(current)
```
</details>
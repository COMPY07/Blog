---
title: "[BOJ] 0과 1 - 2"
published: 2024-06-18
description: 8112 math (N % M) % M = N % M 을 이용하기
image: ""
tags: [ps, algorithm, boj]
category: CS
draft: false
---

# [0과 1 - 2](https://www.acmicpc.net/problem/8112)

| TimeLimit | MemoryLimit |             Condition             |   TAG    |
|:---------:|:-----------:|:---------------------------------:|:--------:|
|    1s     |    256MB    |  (T <= 10, 1 <= N <= 1,000,000)   | Math(수학) |


> 폴란드 왕자 구사과는 다음과 같은 수를 좋아한다.
> * 0과 1로만 이루어져 있어야 한다.
> * 1이 적어도 하나 있어야 한다.
> * 수가 0으로 시작하지 않는다.
> 예를 들어, 101은 구사과가 좋아하는 수이다.
> 자연수 N이 주어졌을 때, N의 배수이면서, 구사과가 좋아하는 수 중에서 가장 작은 수를 구하는 프로그램을 작성하시오.


이번 문제는 직관적으로 "음 어떻게 풀어야지"라는 생각이 들지 않았다. 그래서 생각보다 많은 시간을 아이디어 구상하는데 
쏟아 부었다. 

조건을 다시한번 살펴보자

> * 0과 1로만 이루어져 있어야 한다.
> * 1이 적어도 하나 있어야 한다.
> * 수가 0으로 시작하지 않는다.

0과 1로만 이루어져 있다는 것은 알겠고,
1이 적어도 "하나"이상 있어야 한다는 것도 알겠다.
또 0으로 시작하는 수는 없으니 조건은 당연한 얘기를 하고있다.

그러면 조건이 문제가 아니라 그냥 "자연수 N이 주어졌을 때, N의 배수이면서, 구사과가 좋아하는 수 중에서 가장 작은 수"를
구하는 것 자체가 문제인 것이다. 진짜 빡센 문제처럼 보인다.

<br>
나는 이러한 유형의 문제가 생소하기도 했고, 생각하는 것이 여려웠으나 생각을 오랬동안 하다보니 방법이 떠올라 문제를 어찌저찌 풀게되었다.

<br>
<br>
<br>
<br>
<br>

일단 문제를 풀기 위해서 아래의 식의 이해가 필요하다.

정수 N과 M이 존재할 때,
### N%M = (N%M) % M
정말 이 식을 보았을 때, "당연하거 아니야?"라고 생각할실 텐데 이게 문제에서 코드로 적용하면 좀 새롭게 다가옵니다.



```py
# par가 string이라고 할 때,
((mod * 10) % n, par+"0") 
(mod * 10 + 1) % n, par + "1")
```

이런 수식을 통해서 Q에 넣고, 쭉 돌면서 원하는 좋아하는 수를 찾아내는 겁니다.

그러다가 mod % n == 0이 되면 현재 돌고 있던, par를 반환하면서 찾아냅니다.

이를 통해서 우리가 원하는 수를 찾아낼 수 있습니다.

물론 visited 처리는 무조건 필요합니다. 아니면 메모리, 시간초과 걸리게 되면서 눈물 찔끔 나옵니다.

<details>
<summary>정답 코드</summary>

<!-- summary 아래 한칸 공백 두어야함 -->

```py
import sys
from collections import deque
input = sys.stdin.readline
def solution():

    n = int(input())
    visited = [False] * 1000000
    result = [0] * 1000001
    result[0] = 1
    q= deque([(1, "1")]) # 나머지, parent

    while q:
        mod, par = q.popleft()
        if visited[mod]: continue

        if mod % n == 0: return par
        # elif (mod+1) % n == 0: return par[:-1]+"1"
        visited[mod] = True
        q.append(((mod * 10) % n, par+"0"))
        q.append(((mod * 10 + 1) % n, par + "1"))
        #print(q)
    return "BRAK"

for i in range(int(input())): print(solution())
```



---
title: "[BOJ] 수식 표현"
published: 2024-06-12
description: dynamic programming을 이용한 문제 풀이
image: cover.png
tags: [ps, algorithm, boj]
category: CS
draft: false
---

https://www.acmicpc.net/problem/1955

| TimeLimit | MemoryLimit |    Condition     |              TAG              |
|:---------:|:-----------:|:----------------:|:-----------------------------:|
|    1s     |    128MB    | (1<= N <=10,000) | Math, DP(dynamic programming) |

<br>

이 문제를 보면 갑자기 겁이 들 수도 있을 것 같다. 하지만 사실 문제 자체가 너무 간단하기 때문에
그렇게 겁먹지 않아도 된다.

> 수식 표현이란 1, +, *, !, (, )로만 이루어진 수식을 말한다. 간명하게 정의하기 위해, 다음과 같이 귀납적으로 정의할 수 있다.
> 1. 1은 수식표현이다.
> 2. e가 수식표현이면 (e)와 e!도 수식표현이다.
> 3. e1과 e2가 수식표현이면 e1+e2와 e1*e2도 수식표현이다.
> 
> 예를 들어 18의 수식표현은 (1+1+1)*(1+1+1)!, (1+1+1+1)*(1+1+1) +(1+1+1)! 등이 있다. 우리는 n이 주어졌을 때, n의 값을 갖는 수식표현을 구하고 싶다. 단, 1의 개수를 최소로 사용하는 것이어야 한다.



<br>

문제를 분석해보자면 숫자 1과 연산자들만 사용해서 입력으로 들어오는 N을 만드는 것을 찾는데,
여기서 중요한건 1을 최대한 적게 사용하는 것이다.

<br>

생각을 조금만 해본다면 "e1과 e2가 수식표현이면 e1+e2와 e1*e2도 수식표현이다."라는 것을 본다면
아 작은 것부터 제일 적은 표현법을 찾고, 그를 통해서 큰 수를 확장해 나가면 되겠구나라고 생각할 수 있다.

<br>

```cpp
int dp[100'001] = {MAX, };


int fact(int current){
    if(current == 1) return 1;
    return fact(current-1) * current;
}
int main(){
    int n;
    for(int i = 0; i <= 10000; i++) dp[i] = MAX;
    // 7! 이후 부터는 !쓰지 않음.
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    dp[4] = 4;
    dp[5] = 5;
    dp[6] = 3;
    dp[7] = 4;
    
    cin >> n;
    
    for(int i = 1; i <= n; i++){
        dp[i] = min({dp[i], dp[i-1]+1});
        for(int j = 2; j <= i; j++){
            if(j*i < 10001) dp[i*j] = min(dp[i*j], dp[i] + dp[j]);
            if(i+j < 10001) dp[i+j] = min(dp[i+j], dp[i] + dp[j]);
        }
        if(i < 8) dp[fact(i)] = dp[i];
    }
    
    cout << dp[n];
    
}
```

이 코드를 하나하나 분석해 보겠다.


<br>

* 0을 표현하는 1은 0개
* 1은 1개 / 1
* 2는 2개 / 1+1
* 3은 3개 / 1+1+1
* 4는 4개 / 1+1+1+1
* 5는 5개 / 1+1+1+1+1
* 6은 3개 / (1+1+1)!
* 7은 4개 / 6+1

이것을 미리 해놓은 이유는 
좀 편하게 팩토리얼 값을 넣어놓고 시작하기 위해서 넣어놓았습니다.

이제는 for문이 도는 원리를 설명하자면,

<br>

현재 내 자신과 전에 있던 조합에서 1을 더한 것 중에 1이 더 적게 쓰인 것을 선택합니다.

또한 자기 자신에서 자기보다 작은 값과의 곱과 합을 통해서 다음 큰 수들의 최솟값을 다시 업데이트함으로써

20을 4*5 의 최소 1의 개수를 얻을 수 있도록 설계하였습니다.

fact은 7로 제한하였는데 이유는 8!이 n의 최댓값을 넘어가기 때문에 조건을 걸어주었습니다.



<details>
<summary>정답보기</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
## Solution
```cpp
#define MAX 2'100'000'000
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <math.h>
#include <random>

#include <stdlib.h>
#include <time.h>
#include <stdio.h>


using ll = long long;
using ull = unsigned long long;
using namespace std;
// int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1}, dx[] = {0, -1, -1, -1, 0, 1, 1, 1}; // up, lup, left, ldown, down, rdown, right, rup

int dp[100'001] = {MAX, };


int fact(int current){
    if(current == 1) return 1;
    return fact(current-1) * current;
}
int main(){
    int n;
    for(int i = 0; i <= 10000; i++) dp[i] = MAX;
    // 7! 이후 부터는 !쓰지 않음.
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    dp[4] = 4;
    dp[5] = 5;
    dp[6] = 3;
    dp[7] = 4;
    
    cin >> n;
    
    for(int i = 1; i <= n; i++){
        dp[i] = min({dp[i], dp[i-1]+1});
        for(int j = 2; j <= i; j++){
            if(j*i < 10001) dp[i*j] = min(dp[i*j], dp[i] + dp[j]);
            if(i+j < 10001) dp[i+j] = min(dp[i+j], dp[i] + dp[j]);
        }
        if(i < 8) dp[fact(i)] = dp[i];
    }
    
    cout << dp[n];
    
}


```
</details>
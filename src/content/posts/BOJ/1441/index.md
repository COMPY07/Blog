---
title: "[BOJ] 나누어 질까"
published: 2024-06-25
description: 생각만 하면 풀 수 있어요...
image: ""
tags: [algorithm, ps]
category: CS
draft: false
---

[나누어 질까](https://www.acmicpc.net/problem/1441)
------------

| TimeLimit | MemoryLimit |            Condition            |      TAG |
|:---------:|:-----------:|:-------------------------------:|:--------:|
|    2s     |    128MB    | (1<= N <=18, 1 <= L, R <= 10^9) | Math(수학) |


> 어떤 숫자 배열 A가 주어지면, L보다 크거나 같고, R보다 작거나 같은 자연수 중에, A에 속해있는 원소 중 적어도 하나로 나누어지는 수의 개수를 구하는 프로그램을 작성하시오.


문제는 정말 간단하지만, 풀이를 생각하는데 꽤 많은 시간이 걸렸다.
일단 최소 공배수를 구하고, 이를 통해서 중복되는 것을 제외한 각 원소들의 배수들의 개수를 더하면 되는 문제입니다.

이걸 어떻게 풀 수 있을까요??

먼저 LCM(최소 공배수)를 구하는 방법은

```cpp
ll lcm(int a, int b){
    return (a*b) / gcd(a, b);
}
```

이렇게 구현할 수 있다.

gcd의 구현은 "유클리드 호제법"을 이용해서 최적의 방법으로 구현이 가능하다.
이후에 경우의 수를 다 더하면 되는데, 이걸 어떻게 **시간초과를 피하고**, 정확하게 값을 출력할 수 있을까?
내가 해결한 방법의 힌트를 소개하겠다.

함수 f는 파라미터로 들어오는 n의 l부터 r까지의 배수의 개수를 가져오는 함수라고 정의한다.

**f(n) = r/lcm(n) - l/lcm(n) + !(l%lcm(n))**

이렇게 표현할 수 있다.

**r > l이 언제나 성립**하기 때문에 문제가 없으며, !(l%f(n))은 나머지가 나오지 않는다면, 나누어 떨어지기 때문에 "l 이상"의 조건에 의해서 l까지 포함시켜 더한다.

자 일단 이러한 함수를 가지고 하나의 문제를 풀어보겠다.

------------

2 3 5라는 원소가 들어왔다고 치자.

l이 1이고, r이 100이라고 가정하자.

f(2) + f(3) + f(5)가 기본적으로 있을 것이고, 이제 겹치는 것들을 빼야한다.

2, 3의 최소 공배수 **f(6)을 빼고**,
2, 5의 최소 공배수 **f(10)을 빼고**,
3, 5의 최소 공배수 **f(15)를 뺀다**.

이렇게 뺄 때, 또 중복돼서 빼지는 수가 생기게 된다. 바로 2, 3, 5의 공배수가 3번 빠지기 때문에 개수 카운트가 전혀 안되는 것이다.
그래서 우리는 f(30)을 더해줄 것이다.

이제 뭔가 규칙이 보이죠??

바로 N개의 원소들로 공배수를 찾고서 빼거나 더할 때, 그 조건이 N개의 짝수, 홀수 여부라는 것을 알겠죠?


이제는 바로 문제를 풀어보자.



코드 풀이
--------------

### 유클리드 호제법
```cpp
ull gcd(ull a, ull b){
    if(b == 0) return a;
    return gcd(b, a%b);
}

ull lcm(ull a, ull b){
    return (a*b) / gcd(a, b);
}
```

### solution
그냥 bruteforce로 돌면서 그 조합에 대한 모든 경우를 빼고, 더하기를 하였다.
cpp의 대한 코드를 이해할 수만 있다면, 코드 이해는 쉬울 것이라고 생각한다.
```cpp
ll solution(int depth, vector<int> &current, int idx){
    ll result = 0;
    
    ull mylcm = 1;
    
    for(int num : current){
        mylcm = lcm(num, mylcm);
        if(mylcm > r) return result;
    }
    result+=(r/mylcm - l/mylcm + !(l%mylcm)) * (depth%2 ? -1 : 1);
    for(int i = idx+1; i < n; i++){
        current.push_back(nums[i]);
        result+= solution(depth+1, current, i);
        current.pop_back();
    }
    
    return result;
}
```

### Main

이또한 코드에 이해가 안되진 않을 것이라 판단했다.
위에서 설명한 그대로의 식을 사용하여 구현한 것이라, 딱히 문제가 되진 않는다.
```cpp
int main(){
    cin >> n >> l >> r;
    result_num = 0;
    vector<ull> real;
    for(int i = 0; i < n; i++){
        cin >> nums[i];
        result_num += r/nums[i] - l/nums[i] + !(l%nums[i]);
    }
    
    
    sort(nums, nums+n);
    
    vector<int> val;
    ll plus_value = 0;
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            val.push_back(nums[i]);
            val.push_back(nums[j]);
            plus_value += solution(1, val, j);
            val.pop_back();
            val.pop_back();
        }
    }
    
    cout <<  result_num + plus_value;
    return 0;
    
}
```


구현에서 어려웠던 것은 처음 overflow를 고려하지 못한 점이 너무나 컷다 그것 때문에 많은 시간을 허비했는데
요즘따라 overflow에 많이 당하고 있는데도 계속 당하는걸 보니 아직도 부족한가 보다.

여러분도 조심하셔요!

<details>
<summary> 정답 코드 </summary>

```cpp
#define MAX 2'100'000'000
#define limit 10'000'000'000
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <math.h>
#include <random>
using namespace std;

using ull = unsigned long long;
using ll = long long;


ull gcd(ull a, ull b){
    if(b == 0) return a;
    return gcd(b, a%b);
}

ull lcm(ull a, ull b){
    return (a*b) / gcd(a, b);
}

int nums[20];
ull result_num;
ll l, r;
int n;


ll solution(int depth, vector<int> &current, int idx){
    ll result = 0;
    
    
    ull mylcm = 1;
    for(int num : current){
        mylcm = lcm(num, mylcm);
        if(mylcm > r) return result;
    }
    result+=(r/mylcm - l/mylcm + !(l%mylcm)) * (depth%2 ? -1 : 1);
    for(int i = idx+1; i < n; i++){
        current.push_back(nums[i]);
        result+= solution(depth+1, current, i);
        current.pop_back();
    }
    
    
    return result;
}
bool visited[20];
int main(){
    cin >> n >> l >> r;
    result_num = 0;
    vector<ull> real;
    for(int i = 0; i < n; i++){
        cin >> nums[i];
        result_num += r/nums[i] - l/nums[i] + !(l%nums[i]);
    }
    
    
    sort(nums, nums+n);
    
    vector<int> val;
    ll plus_value = 0;
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            val.push_back(nums[i]);
            val.push_back(nums[j]);
            plus_value += solution(1, val, j);
            val.pop_back();
            val.pop_back();
        }
    }
    
    cout <<  result_num + plus_value;
    return 0;
    
    
}
```
</details>
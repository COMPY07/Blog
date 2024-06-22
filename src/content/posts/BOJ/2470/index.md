---
title: "[BOJ] 두 용액"
published: 2024-06-22
description: 2470 two pointer 해설
image: ""
tags: [ps, algorithm]
category: CS
draft: false
---

# [두 용액](https://www.acmicpc.net/problem/2470)


| TimeLimit | MemoryLimit |                                              Condition                                               |     TAG    |
|:---------:|:-----------:|:----------------------------------------------------------------------------------------------------:|:----------:|
|    1s     |    128MB    |                      (2 ≤ N ≤ 100,000,-1,000,000,000 ≤ element ≤ 1,000,000,000)                      | TwoPointer |




> KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다.
> 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.
> 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고,
> 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.<br><br>
> 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
> 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.<br><br>
> 예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다.<br>
> 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.<br><br>
> 산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 **0에 가장 가까운 용액을 만들어내는 두 용액을 찾는** 프로그램을 작성하시오.



우리의 목표는 **"주어진 수(0을 제외한 범위 안에 정수)들 중에서 서로다른 2개를 골라서 0에 가장 가까운 수를 만들어라."** 이다.



여기서 제일 먼저 생각해볼 것은 어떻게 0에 가까운 수를 만들 것인가? 이다.



여러가지를 생각해보자! 

1. BruteForce
2. Sort 
3. Two Pointer

이렇게 3가지를 생각해보자.



일단 먼저 전체를 탐색하는 BruteForce이다.

N의 최댓값인 100,000으로 계산을 해보자면 모든 수들과 다하고 비교하는 과정에서 최악의 경우엔 N^2 즉 O(N^2)이 되므로 시간초과에 걸리게 된다.

<br>
<br>

다음으론 Sort이다. 정렬을 하여 작은 수, 큰 수들끼리 더해서 0에 가까운 수를 만들어내는 방법이다. 사실상 이것도 정확히 어떤 값이 0에 가까운 수인지 모르기 때문에 넘어간다.



<br>


마지막으로 TwoPointer이다. 일단 문제에서 "2개의 용액을 골라서"를 보자마자 이 방법으로 접근해야 되겠다고 생각이 들었다. 투 포인터로 접근하세요!라고 문제에서 말하고 있어서 나는 3번째 방법인 투 포인터로 접근하여 문제를 풀이하였다.

내가 선택한 방법은 일단 받은 모든 용액들을 오름차순으로 정렬 후, 각 끝(제일 작은 수, 제일 큰 수)부터 시작하여 0을 기점으로 큰지 작은지를 판단 후 작은 수 쪽의 값을 큰 값 쪽으로 당기거나 큰 수 쪽의 값을 작은 수 쪽으로 당기는 방법으로 0과 제일 가까운 수를 알아내도록 하였다.


일단 내가 말한 내용을 정리해 보자면,



투 포인터로 풀이하기 위해서 작은 수와 큰 수들이 모여있는 곳을 나눈다.(단조화)
작은 쪽 수에서 시작하는 포인터(left), 큰 쪽 수에서 시작하는 포인터(right) 이 2개의 포인터로 0에 가까운 용액을 찾아낸다.
현재 left와 right가 가르키고 있는 용액이 0보다 크다면, 작다면으로 나누어 right를 left쪽으로 당기거나, left를 right쪽으로 당겨와 다시 반복해 제일 0과 가까운 수를 찾도록 한다.
이렇게 요약할 수 있다.

1. 단조화
2. left, right의 포인터 시작
3. left-> 큰 수쪽으로, right -> 작은 수 쪽으로 탐색 시작
4. 최적의 해 찾음.




<br>


이제 코드로 확인해 보자!

<br><br>



전역 변수
------------------
```cpp
int n;

vector<int> nums;
```
* N
  * 몇 개의 용액이 들어오는지 알려주는 변수
* nums
  * 각 용액의 특성값을 저장하는 벡터
----------------

Main
----------
```cpp
int main(){
    fast_io
    
    cin >> n;
    nums.resize(n);
    
    for(int i = 0; i < n; i++) cin >> nums[i];
    
    sort(nums.begin(), nums.end());
    
    int left= 0, right = n-1;
    pair<int, int> result = {MAX, 0};
    
    while(left < right){
        if(diff(result.first, result.second) > diff(nums[left], nums[right])) result = {nums[left], nums[right]};
        
        if((nums[left] + nums[right]) < 0) left++;
        else right--;
    }
    
    cout << result.first << " "<< result.second;
    
}
```
<br>

main은 입력을 받고, 바로 투 포인터를 이용해서 두 용액의 합이 0과 가장 가까운 두 용액을 구하는 코드입니다.



sort는 C++ STL(algorithm에 존재)에 내장 함수입니다.



sort를 통해서 정렬해주고, 가장 작은 수부터 시작하는 left, 가장 큰 수부터 시작하는 right를 인덱스로 초기화 해줍니다.



diff는 간단히 abs(용액1+용액2)의 연산을 해주는 함수입니다.



현재 등록되어있는 두 용액의 합보다 지금 가르키고 있는 두 용액의 합이 0에 더 가깝다면, result를 업데이트 해줍니다.



또한 현재의 합이 0보다 작다면 더 큰 값으로 탐색할 수 있게 left를 +1하고, 합이 0보다 크거나 같다면 right-- 해줍니다.



여기서 같다면 어차피 위에서 result가 업데이트 되었기 때문에 상관할 같은 상황은 고려할 필요가 없습니다.

-----------


<br>
<br>

이렇게 반복하면서 left와 right가 크로스될 때까지 돌게된다면, 간단히 두 용액의 합이 0에 가장 가까운 두 용액을 얻어낼 수 있습니다.

참 간단하죠잉?

다들 즐거운 PS 하세용!!

<details>
<summary> 정답 코드 </summary>

```cpp
#define MAX 2'100'000'000
#define LLMAX 9'223'372'036'854'775'807
#define fast_io ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <ctime>
#include <stdio.h>
using ll = long long;
using ull = unsigned long long;
using namespace std;

int n;

vector<int> nums;

int diff(int a, int b){ return abs(a + b); }

int main(){
    fast_io
    
    cin >> n;
    nums.resize(n);
    
    // 1 상근, 0 창영
    
    // 1 0 1 1 0 1 0 0
    
    for(int i = 0; i < n; i++) cin >> nums[i];
    
    sort(nums.begin(), nums.end());
    
    int left= 0, right = n-1;
    pair<int, int> result = {MAX, 0};
    
    while(left < right){
        if(diff(result.first, result.second) > diff(nums[left], nums[right])) result = {nums[left], nums[right]};
        
        if((nums[left] + nums[right]) < 0) left++;
        else right--;
    }
    
    cout << result.first << " " << result.second;
    
}
```

</details>
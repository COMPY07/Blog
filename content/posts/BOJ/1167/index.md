---
title: "[BOJ] 트리의 지름"
published: 2024-06-28
description: DFS를 이용한 그래프 탐색
image: ""
tags: [algorithm, ps]
category: CS
draft: false
---

## [트리의 지름](https://www.acmicpc.net/problem/1167)

> 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

문제는 너무나 간단합니다. 사실 말할 필요도 없이, 그냥 주어진 cost만을 가지고 길이를 더해가면서 측정하면 끝이기 때문입니다.

입력을 제외한 핵심 DFS 코드만 살펴보고 프스트를 마무리하겠습니다.

```cpp
vector<pair<int, int>> tree[100'001];
bool visited[100'001];
int result = 0;

int solution(int current, int length_){
   
    
    int length = 0;
    int child_max = 0;
    int child_second = 0;
    
    visited[current] = true;
    
    for(pair<int ,int> next : tree[current]){
        if(visited[next.first]) continue;
        int result = solution(next.first, child_max) + next.second;
        if(child_max < result){
            length = child_max+result;
            child_second = child_max;
            child_max = result;
        }else if(child_second < result){
            length = child_max + result;
            child_second = result;
        }
    }
    
    result = max({child_max+child_second,
                result,
                child_max + length_});
    
    return child_max;
}
```
> 전역 변수
> * tree
>  * 말 그대로 트리의 정보를 담는 배열
> * visited
>   * 방문한 노드인지 확인하는 배열
> * result
>   * 출력할 결과값
> 
> 파라미터
> * current
>   * 현재 자신의 노드 위치
> * length_
>   * 전에 있던 노드에서 제일 깊게 탐색되었던 길이
> 
> 지역 변수
> * length
>   * 일단 선언해 두고서, 쓰지 않은 변수
> * child_max
>   * 자식 중에서 제일 먼 거리
> * chlid_second
>   * 자식 중에서 두번째로 먼 거리



이 코드는 정말 직관적이라 설명이 필요 없을 듯하다.

overflow도 조심할 필요가 없었기 때문에 쉽게 풀이하였다.


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

int n;

vector<pair<int, int>> tree[100'001];
bool visited[100'001];



int result = 0;

int solution(int current, int length_){
   
    
    int length = 0;
    int child_max = 0;
    int child_second = 0;
    
    visited[current] = true;
    
    for(pair<int ,int> next : tree[current]){
        if(visited[next.first]) continue;
        int result = solution(next.first, child_max) + next.second;
        if(child_max < result){
            length = child_max+result;
            child_second = child_max;
            child_max = result;
        }else if(child_second < result){
            length = child_max + result;
            child_second = result;
        }
    }
    
    result = max({child_max+child_second, result, child_max + length_});
    
    return child_max;
}


int main(){
    cin >> n;
    
    
    int current_node;
    for(int i = 0; i < n; i++){
        cin >> current_node;
        
        int node = 0, cost_;
        while(node != -1){
            cin >> node;
            if(node == -1) break;
            cin >> cost_;
            
            tree[current_node].push_back({node, cost_});
            tree[node].push_back({current_node, cost_});
            
        }
    }
    
    solution(1, 0);
    cout << result;
    
    
    
    
    return 0;
}
    
```
</details>
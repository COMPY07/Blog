---
title: "[BOJ] 연구소"
published: 2024-04-10
description: 14502 bfs, bruteforce 풀이
image: cover.png
tags: [ps, algorithm, boj]
category: CS
draft: false
---

** https://www.acmicpc.net/problem/14502 **

|  TimeLimit  |  MemoryLimit  |  Condition   |               TAG                |
|:-----------:|:-------------:|:------------:|:--------------------------------:|
|     2s      |     512MB     | (3<=N,M<=8)  |  BFS(너비 우선 탐), BruteForce(전체탐색)  |


일단 문제가 자체가 너무 BFS로 푸세요!!를 내뿜고 있어서 바로 BFS로 접근했다.

> 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
> 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
> 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
> 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
>> 2 0 0 0 1 1 0\
>> 0 0 1 0 1 2 0\
>> 0 1 1 0 1 0 0\
>> 0 1 0 0 0 0 0\
>> 0 0 0 0 0 1 1\
>> 0 1 0 0 0 0 0\
>> 0 1 0 0 0 0 0
>
> 이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
> 2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.
>> 2 1 0 0 1 1 0\
1 0 1 0 1 2 0\
0 1 1 0 1 0 0\
0 1 0 0 0 1 0\
0 0 0 0 0 1 1\
0 1 0 0 0 0 0\
0 1 0 0 0 0 0
> 
> 바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
>> 2 1 0 0 1 1 2\
1 0 1 0 1 2 2\
0 1 1 0 1 2 2\
0 1 0 0 0 1 2\
0 0 0 0 0 1 1\
0 1 0 0 0 0 0\
0 1 0 0 0 0 0
> 
> 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.
> 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.


우리가 문제에서 집중해야 되는 것은 바로 "일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다." 이 문장이다. 또한 grid(격자) 문제 답게 상하좌우로 이동할 수 있다고 문제에서 말하고 있다. "0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다." 이렇게 우리가 얻은 정보는



* 벽의 개수는 3개이며 "꼭" 모두 세워야한다.
* 바이러스는 동서남북으로 한 턴마다 확산된다.
* 바이러스는 벽을 이동하지 못 한다.
* 안전 영역이 가장 큰 경우를 구해야됨.


&nbsp;


이제 문제를 파악했으니, 어떤 기능이 있어야 되는지를 정리해보자.


* 바이러스가 퍼지는걸 돌려줄 BFS 함수
* 벽을 3개 세워줄 벽세우는 함수
* main

이 정도로 줄여줄 수 있을 것이다.
\
&nbsp;
\
&nbsp;


코드를 하나하나 짜보자!!

\
&nbsp;

* 전역변수

> 
> 
> ```cpp
> using ll = long long;
> using namespace std;
> int dy[] = {0, 0, -1, 1}, dx[] = {1, -1, 0, 0};
> int n, m;
> int board[10][10];
> vector<pair<int, int>> origin;
> vector<pair<int, int>> position;
> int count_ = 0;
> int res = 0;
> ```
> * dy, dx
> * * 동서남북으로 움직일 바이러스의 경로를 for문으로 간단 처리하기 위해서
> * n, m
> * * 입력으로 n*m 크기의 연구소가 주어지기 때문에 입력받을 크기
> * origin
> * * 바이러스의 위치를 담은 vector
> * position
> * * 빈칸의 위치를 담은 vector
> * board
> * * n*m 크기의 연구실(바이러스, 빈 칸, 벽의 위치를 담고 있음)
> * count_
> * * 빈 공간의 크기(개수)
> * res
> * * result 값



```cpp
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    cin >> n >> m;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m;j++){
            cin>>board[i][j];
            if(board[i][j] == 2){
                origin.push_back(make_pair(i, j));
                board[i][j] = 0;
                count_++;
            }
            else if(board[i][j] == 0){
                count_++;
                position.push_back(make_pair(i, j));
            }
            
        }
    }
    
    int result = rec(3, 0) - 3;
    cout << result;
    
}
```

ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0); 빠른 입출력을 하는 코드입니다.



먼저 n, m을 받습니다.



그 후 n*m 만큼 반복문을 돌면서 각 위치마다의 정보를 저장합니다.



바이러스이면 origin에 넣고, 빈 공간이면 position에 좌표를 저장합니다.





다음으로 3개의 벽을 세울 코드를 짜보자!

```cpp
int rec(int current, int start){
    if(current <= 0){
        queue<pair<int, int>> q;
        for(pair<int, int> item : origin) q.push(item);
        int tmp[10][10];
        memcpy(tmp, board, sizeof(board));
        return solution(q, tmp, count_);
    }
    int result = 0;
    for(int i = start; i < position.size(); i++){
        pair<int, int> item = position[i];
        board[item.first][item.second] = 1;
        result = max(rec(current-1, i+1), result);
        board[item.first][item.second] = 0;
    }
    return result;
}
```

저는 재귀적으로 배치하고 solution이라는 BFS 함수를 호출해서 개수를 세도록 코드를 작성하였습니다.



약간의 백트래킹 느낌으로 current가 초기에 3이고, 그 후 1씩 감소하면서 3개의 벽을 생성 후 BFS를 돌리는 식으로 설계했습니다.



이제 마지막으로 BFS를 돌리는 solution에 대해서 보도록 하자
```cpp
int solution(queue<pair<int, int>> q, int bor[10][10], int cnt){

    int x, y, ny, nx;
    while(!q.empty()){
        pair<int, int> pos = q.front();
        
        q.pop();

        x = pos.second;
        y = pos.first;
        if(bor[y][x] != 0) continue;
        bor[y][x] = 2;
        cnt--;

        for(int i = 0; i < 4; i ++){
            ny = y + dy[i];
            nx = x + dx[i];
            if(0 <= ny && ny < n && 0 <= nx && nx < m && bor[ny][nx] == 0) q.push(make_pair(ny, nx));
        }
    }
    return cnt;
}
```
solution은 q에 넣어놓은 바이러스들을 차례대로 확산시키면서 큐가 empty가 될 때까지 돌도록 하였습니다.



한번 방문한 위치에는 2로 업데이트 후 다시 동서남북으로 확상되도록 만들었습니다.



if문은 혹시나 board의 범위 밖으로 나가는 것을 방지하기 위해서 작성된 조건문입니다.



이렇게 나온 count는 벽을 포함한 빈 공간의 개수이므로 -3을 통해서 최대 빈 공간의 개수를 알 수 있습니다.



***정답코드***
<details>
<summary>정답보기</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
## Solution
```cpp
#define MAX 200000001
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>
using ll = long long;
using namespace std;

int dy[] = {0, 0, -1, 1}, dx[] = {1, -1, 0, 0};

int n, m;
int board[10][10];

vector<pair<int, int>> origin;
vector<pair<int, int>> position;
int count_ = 0;
int res = 0;
int test = 0;

int solution(queue<pair<int, int>> q, int bor[10][10], int cnt){

    int x, y, ny, nx;
    while(!q.empty()){
        pair<int, int> pos = q.front();
        
        q.pop();

        x = pos.second;
        y = pos.first;
        if(bor[y][x] != 0) continue;
        bor[y][x] = 2;
        cnt--;

        for(int i = 0; i < 4; i ++){
            ny = y + dy[i];
            nx = x + dx[i];
            if(0 <= ny && ny < n && 0 <= nx && nx < m && bor[ny][nx] == 0) q.push(make_pair(ny, nx));
        }
    }
    return cnt;
}

int rec(int current, int start){
    if(current <= 0){
        queue<pair<int, int>> q;
        for(pair<int, int> item : origin) q.push(item);
        int tmp[10][10];
        memcpy(tmp, board, sizeof(board));
        return solution(q, tmp, count_);
    }
    int result = 0;
    for(int i = start; i < position.size(); i++){
        pair<int, int> item = position[i];
        board[item.first][item.second] = 1;
        result = max(rec(current-1, i+1), result);
        board[item.first][item.second] = 0;
    }
    return result;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> n >> m;
    
    
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m;j++){
            cin>>board[i][j];
            if(board[i][j] == 2){
                origin.push_back(make_pair(i, j));
                board[i][j] = 0;
                count_++;
            }
            else if(board[i][j] == 0){
                count_++;
                position.push_back(make_pair(i, j));
            }
            
        }
    }
    
    int result = rec(3, 0) - 3;
    cout << result;
    
}
```
</details>





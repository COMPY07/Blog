---
title: "[BOJ] 치즈"
published: 2024-07-01
description: 자 치즈!!
image: ""
tags: [algorithm, ps]
category: CS
draft: false
---


[치즈](https://www.acmicpc.net/problem/2638)

| TimeLimit | MemoryLimit |     Condition     |     TAG     |
|:---------:|:-----------:|:-----------------:|:-----------:|
|    1s     |    128MB    | (5<= N, M <= 100) | BFS(너비우선탐색) |

>N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다. 단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다. 따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.
> 
> <그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다. 그러므 로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다. 그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.
> 
> 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.
> 
>(그림은 boj를 참고해 주세요)


문제를 읽어보니 대충 요약을 해보자면 **"격자로 구성되어 있는 치즈 중에서 '바깥 공기'와 '두 변이 접촉'한 치즈는 다음 시간에 사라진다. 모든 치즈가 사라진 정확한 시간을 구하는 것이 목표"** 로 말할 수 있다.



요약한 내용과 문제에서 주어진 정보들을 정리해 보자면



* 치즈는 '바깥 공기'와 '두 변이 접촉'하면 녹는다.
* 모든 치즈가 사라지지 않는 경우의 수는 없다.(어떻게든 두 변이 닿는 치즈가 존재함)
* 치즈가 녹는 시간은 접촉과 동시에 정확히 1시간이다.


우리가 해결해야될 문제들을 더욱 구체화 시켜서 보도록 하자.(구현해야될 기능 정리)



* 녹는 치즈들을 선별해내는 기능
* 녹는 치즈들이 없어지고, 다음 공기(바깥 공기가 아닌)들과 접촉되는 기능
* BFS에서 시간 복잡도와 공간 복잡도를 최적화하기 위해서 visited.



<details>
<summary>전역 변수들</summary>

```cpp
int n, m;
bool board[102][102], visited[102][102];
int costBoard[102][102];
bool test[102][102];
int dy[] = {1, -1, 0, 0}, dx[] = {0, 0, 1, -1};
int result = 0, cnt = 0;
queue<pair<int, int>> q, air;
```

* N, M
  * 입력으로 주어지는 n*m 크기의 치즈가 들어온다고 알려주는 2개의 크기 값.
* board
  * board[y][x]값이 true이면 치즈, false이면 공기라는 것을 저장하는 2차원 배열
* visited
  * visited[y][x]가 방문했었는지의 정보를 저장하고 있는 2차원 배열
* costBoard
  * costBoard[y][x]는 바깥 공기와 몇 개의 변이 닿아있는지를 저장하는 2차원 배열
* dy, dx
  * 동서남북으로 확산되는 것을 for문으로 간단히 처리하기 위해서 선언한 배열
* result
  * 현재 몇 시간이 지났는지 저장하는 변수
* cnt
  * 현재 녹지않은 치즈의 개수
* Q
  * "한" 시간에 녹아내릴 치즈를 알아내는 Queue
* air
  * 공기들이 순차적으로 들어와 순회하면서 치즈를 녹일 수 있도록하는 Queue
</details>

<br>

전역 변수들을 선언하고 이제 main으로 들어가보자

```cpp
#define fast_io ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int main(){
    fast_io
    cin >> n >> m;
    
  
    
    int tmp;
    
    
    for(int i = 1; i <= n; i++){
        
        for(int j = 1; j <= m; j++){
            cin >> tmp;
            board[i][j] = tmp;
            if(board[i][j]) cnt++;
        }
        if(!board[i][1]) air.push({i, 1});
        if(!board[i][m]) air.push({i, n});
    }
    for(int i = 1; i <= m; i++){
        if(!board[1][i]) air.push({1, i});
        if(!board[n][i]) air.push({n, i});
    }
```

작성된 main의 일부분입니다.



이름부터 알겠지만 fast_io는 빠른 입출력을 해주는 친구들이구요!(C 언어 사용자 분들이 간혹 위에 cin.tie(0)을 쓰시고 scanf를 쓰는 경우를 봤는데요. 그러시면 안됩니다. cin.tie(0)을 사용하시면 cin만 사용해야 됩니다.)



아래부터 입력을 받습니다.



n, m을 먼저 입력받고 n*m만큼 돌면서 치즈를 입력으로 다 받아옵니다.



여기서 "모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정"이 조건을 이용해서 저는 맨 끝의 공기들을 전부 air에 넣어서 탐색을 진행하겠습니다.



if문으로 처리를 해놓은 것은 제가 처음에 저 조건을 못 보고서 모두 처리를 진행했기에 남아있는 겁니당..(index가 1부터 시작하는 것도 그 때문)





이제 주요코드인 BFS 코드를 살펴봅시다.

```cpp
while(!air.empty() && cnt > 0){
        int length = (int) air.size();
        
        for(int i = 0; i < length && cnt > 0; i++){
            
            pair<int, int> pos = air.front(); air.pop();
            if(visited[pos.first][pos.second]) continue;
            q.push(pos);
            board[pos.first][pos.second] = false;
            while(!q.empty() && cnt > 0){
                
                pos = q.front(); q.pop();
                // cout << pos.first << " " << pos.second << "\n";
                if(visited[pos.first][pos.second]) continue;
                if(board[pos.first][pos.second]){
                    costBoard[pos.first][pos.second]++;
                    if(costBoard[pos.first][pos.second] > 1){
                        cnt--;
                        costBoard[pos.first][pos.second] = -MAX;
                        air.push(pos);
                    }
                    continue;
                }
                test[pos.first][pos.second] = true;

                visited[pos.first][pos.second] = true;
                
                
                for(int next = 0; next < 4; next++){
                    int ny = dy[next] + pos.first;
                    int nx = dx[next] + pos.second;
                    
                    if(0 < ny && ny <= n && 0 < nx && nx <= m && !visited[ny][nx]) q.push({ny, nx});
                    
                }
                

            }
            

        }

        result++;
    }
```


코드에서는 먼저 air(바깥 공기들)가 비어있지 않은 상태에서 현재 알고있는 바깥 공기들을 전부 for문을 돌면서 방문하지 않았던 공기를 하나씩 가져옵니다. 그 가져온 공기에서 BFS를 진행시켜서 확산을 통해서 바깥 공기와 접촉한 치즈들을 접촉한 수 만큼 costBoard[치즈의 y 위치][치즈의 x 위치]++을 해줌으로써 닿아있는 변이 하나 더 있다는 것을 세어줍니다. 한번 방문한 공기는 방문처리를 통해서 다시 방문하지 않도록하여, 시간 및 공간을 최적화하였습니다.


그러다 2 변 이상이 한 치즈와 접촉하고 있다면 그 치즈를 다음 시간에는 녹아 없어질 것으로 확정짓고, air에 위치를 넣은 후 다시 재탐색하는 방법으로 접근하였습니다.


이 방법으로 result를 카운트하면 저희가 원하는 "주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간"을 알 수 있습니다.

<details>
<summary> 정답 코드 </summary>

(새벽 감성 코딩이라 좀 이상합니다..)
```cpp
int main(){
    fast_io
    cin >> n >> m;
    
  
    
    int tmp;
    
    
    for(int i = 1; i <= n; i++){
        
        for(int j = 1; j <= m; j++){
            cin >> tmp;
            board[i][j] = tmp;
            if(board[i][j]) cnt++;
        }
        if(!board[i][1]) air.push({i, 1});
        if(!board[i][m]) air.push({i, n});
    }
    for(int i = 1; i <= m; i++){
        if(!board[1][i]) air.push({1, i});
        if(!board[n][i]) air.push({n, i});
    }
    
    
    // cout << cnt << "\n";
    
    while(!air.empty() && cnt > 0){
        int length = (int) air.size();
        
        for(int i = 0; i < length && cnt > 0; i++){
            
            pair<int, int> pos = air.front(); air.pop();
            if(visited[pos.first][pos.second]) continue;
            q.push(pos);
            board[pos.first][pos.second] = false;
            while(!q.empty() && cnt > 0){
                
                pos = q.front(); q.pop();
                // cout << pos.first << " " << pos.second << "\n";
                if(visited[pos.first][pos.second]) continue;
                if(board[pos.first][pos.second]){
                    costBoard[pos.first][pos.second]++;
                    if(costBoard[pos.first][pos.second] > 1){
                        cnt--;
                        costBoard[pos.first][pos.second] = -MAX;
                        air.push(pos);
                    }
                    continue;
                }
                test[pos.first][pos.second] = true;

                visited[pos.first][pos.second] = true;
                
                
                for(int next = 0; next < 4; next++){
                    int ny = dy[next] + pos.first;
                    int nx = dx[next] + pos.second;
                    
                    if(0 < ny && ny <= n && 0 < nx && nx <= m && !visited[ny][nx]) q.push({ny, nx});
                    
                }
                

            }
            

        }

        result++;
    }
    
    cout << result;
    
    return 0;
}
```
</details>
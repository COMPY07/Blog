---
title: "[BOJ] 히스토그램에서 가장 큰 직사각형"
published: 2024-07-07
description: 가장 큰 직사각형!!
image: ""
tags: [algorithm, ps]
category: CS
draft: false
---

[히스토그램에서 가장 큰 직사각형](https://www.acmicpc.net/problem/6549)


| TimeLimit | MemoryLimit |                 Condition                 |      TAG       |
|:---------:|:-----------:|:-----------------------------------------:|:--------------:|
|    1s     |    256MB    | (1<= N <= 100,000<br>0<=h<=1,000,000,000) | Stack(자료구조 스택) |


> 히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.
> ![problem_image](https://www.acmicpc.net/upload/images/histogram.png)
> 히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.


문제는 굉장히 심플한데 대게 이러한 문제들이 걍 어려운것 같다. 
처음 이 문제를 접했을 때 사실 잘 감이 안오긴 했다. 그러다 계속 생각해보니까 스택을 풀이를 할 수 있을 것 같다는 생각이 들어서 구현해서 풀었더니 잘 풀렸던 문제였다.

이러한 유형의 스택 문제를 보통 "모노톤 스택"이라고 부르더라... 나는 사실 알고리즘 이름을 알고 다니진 않아서...
하튼 사실 이러한 유형을 처음 본 나로써는 여기까지 구상하는게 쬐끔 어려웠지만 지금와서는 이러한 방법론을 생각해내는게 조금 익숙해진 것 같다.

나는 이런 문제를 추천한다. 연습하기도 생각하기도 좋은 문제이면서 구현도 꽤 교육적인 것처럼 느껴졌다.(적어도 나는)

자 이제 풀이를 해보겠다.

일단 이 문제는 나처럼 코드를 구현하면 단 한번만의 검사로 끝낼 수 있다.

<br>

```py
rects = list(map(int, input().split()))
if rects[0] == 0: return -1
```
요번 포스팅에서는 입력까지 다뤄보겠다.
먼저 현재 상태가 들어왔다. 만약 이 rects[0]이 0이라면 다음 입력이 없기때문에 함수에서 나온다.


```py
 s = []
 n = rects.pop(0)
 result = 0
```

s는 우리가 사용할 stack이고, n은 바로 현재 그 직사각형의 개수를 나타내기에 빼내준다.

reuslt는 말그대로 정답을 저장할 변수이다.

<br>

```py
for i in range(n):
            while s and rects[s[-1]] > rects[i]:
                h = s.pop()  # height
                w = i - s[-1] - 1 if s else i
                result = result if result > w * rects[h] else w * rects[h]
            s.append(i)
            
```
정말 놀랍겠지만 아이디어만 나온다면 사실 그렇게 긴 코드도 필요 없는거 같다.

코드를 좀 요약해보겠다.



입력 및 종료 조건 확인
* rects = list(map(int, input().split())) : 입력
* if rects[0] == 0: return -1 : 종료 조건

스택 초기화 및 첫 번째 값 처리
* s = [] : 우리가 쓸 스택 초기화
* n = rects.pop(0) : 위에서 설명했죵?
* result = 0 : 결과

직사각형 순회하며 스택에 저장 및 넓이 계산
* for i in range(n): 
* while s and rects[s[-1]] > rects[i] : 현재 직사각형 높이가 스택의 마지막 직사각형 높이보다 작을 때, 스택에서 높이를 꺼내 넓이를 계산합니다.(모노톤 스택)
* h = s.pop() : 스택 top을 꺼내기
* w = i - s[-1] - 1 if s else i : 너비를 계산합니다. 스택이 비어 있으면 i, 비어 있지 않으면 (i - 스택의 마지막 인덱스 - 1)로 계산합니다.
* result = result if result > w * rects[h] else w * rects[h] : 넓이를 계산하여 최대 넓이를 갱신
* s.append(i) : 현재 자기자신 push

남아 있는 직사각형 처리
* while s: : 스택에 남아 있는 직사각형을 모두 처리
* h = s.pop() 
* w = n - s[-1] - 1 if s else n : 너비를 계산
* result = result if result > w * rects[h] else w * rects[h] : 최대 넓이를 갱신

이런 과정을 거치면 처리합니다.


사실 이 문제가 너무 잘 알려져있어서 딱히 써야된다는 생각을 안 하고 있었는데, 어떠한 특별한 일 때문에 
cpp로 짜게되었는데 다시 이 문제를 보니까 굉장히 교육적인 것 같아서 좀 적게 되었다.

오늘도 happy PS 하세용!!


<details>
<summary> 정답 코드 </summary>

```py

def solution():
    while True:
        rects = list(map(int, input().split()))
        if rects[0] == 0: return -1

        s = []
        n = rects.pop(0)
        result = 0

        for i in range(n):
            while s and rects[s[-1]] > rects[i]:
                h = s.pop()  # height
                w = i - s[-1] - 1 if s else i
                result = result if result > w * rects[h] else w * rects[h]
            s.append(i)

        #남은 친구들 다 빼서 처리
        while s:
            h = s.pop()
            w = n - s[-1] - 1 if s else n
            result = result if result > w * rects[h] else w * rects[h]
        # return result
        print(result)

solution()

```


</details>

---
title: "[BOJ] 수학"
published: 2024-06-24
description: 유클리드 호제법을 이용한 1565 풀이
image: ""
tags: [algorithm, ps]
category: CS
draft: true
---

## [수학](https://www.acmicpc.net/problem/1565)

| TimeLimit | MemoryLimit |              Condition               |   TAG    |
|:---------:|:-----------:|:------------------------------------:|:--------:|
|    2s     |    128MB    | (1<= D, M <=50, 0 < Element <= 10^9) | Math(수학) |


> 배열 D와, 배열 M이 주어졌을 때, D에 있는 모든 수의 배수이며, M에 있는 모든 수의 약수인 수의 개수를 구하는 프로그램을 작성하시오.


문제가 원하는 답은 정말 너무나 간단하다. 두 배열이 주어졌을 때, 하나의 배열을 D, 또 다른 배열을 M으로 둔다.
이 때 D의 최소공배수와 M의 최대공약수의 약수의 겹치는 수가 몇개 있는지를 찾아내는 프로그램을 작성하면 된다는 것이다.


먼저 우리는 빠른 시간 안에 최대 공약수와 최소 공배수를 찾는 방법에 대해서 알아보자

## 유클리드 호제법(Euclidean Algorithm)?
--------------------------
### 2개의 자연수의 최대 공약수(Greatest Common Divisor, GCD)를 구하는 알고리즘

:::tip[샹식]
호제법이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
:::

유클리드 호제법은 보통 GCD라는 함수로 구현되어 있습니다.

:::note[핵심]
유클리드 호제법은 Mod 연산(나머지 연산)을 통해서 최대 공약수를 얻어내는 방식이다.

'GCD(A, B) -> A % B -> B % (A%B) -> ....... -> GCD(A, B)'
:::

2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.


-------------------

또한 최대 공약수를 이용해서 최소 공배수를 얻을 수 있는데
이를 이용해서 이 문제를 금방 풀 수 있다.




<details>
<summary> 정답 코드 </summary>

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

var n, m int

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func lcm(a, b int) int {
	return (a * b) / gcd(a, b)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	_, err := fmt.Fscanln(reader, &n, &m)
	if err != nil {
		return
	}

	var tmp int
	fmt.Fscan(reader, &tmp)
	myLcm := tmp
	if tmp == 0 {
		fmt.Fprintln(writer, 0)
		return
	}
	for i := 0; i < n-1; i++ {
		fmt.Fscan(reader, &tmp)
		if tmp == 0 {
			fmt.Fprintln(writer, 0)
			return
		}
		myLcm = lcm(myLcm, tmp)
	}

	fmt.Fscan(reader, &tmp)
	myGcd := tmp

	if tmp == 0 {
		fmt.Fprintln(writer, 0)
		return
	}

	for i := 0; i < m-1; i++ {
		fmt.Fscan(reader, &tmp)
		if tmp == 0 {
			fmt.Fprintln(writer, 0)
			return
		}
		myGcd = gcd(myGcd, tmp)
	}

	if myGcd%myLcm != 0 {
		fmt.Fprintln(writer, 0)
		return
	}

	count := 0
	div := myGcd / myLcm
	for i := 1; i*i <= div; i++ {
		if div%i == 0 {
			count++
			if i != div/i {
				count++
			}
		}
	}

	fmt.Fprintln(writer, count)

}

```
</details>
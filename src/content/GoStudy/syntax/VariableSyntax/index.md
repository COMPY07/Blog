---
title: "[Syntax] Go언어 시작해보자! - Variable(변수) 선언 및 활용"
published: 2024-06-23
description: GO Language의 강력함을 느껴보자
image: ""
tags: [Go]
category: Language
draft: false
---

언어를 배울때 제일 먼저 배우는 것이 바로 **"자료형(data type)"**이다.

이제부터 go에서 사용하는 자료형에 대해서 알아보자!!

먼저 자료형에 대해서 알아본 후, 변수, 상수의 선언 및 초기화에 대해서 다룰 것이다.

<br>

| DataType(자료형) |         Range(범위)         |             Description(설명)              |
|:-------------:|:-------------------------:|:----------------------------------------:|
|     uint      |                           | 부호 X, 32bit(4byte) unsigned integer(정수형) |
|     uint8     |           0~255           | 부호 X, 8bit(1byte) unsigned integer(정수형)  |
|    uint16     |          0~65535          | 부호 X, 16bit(2byte) unsigned integer(정수형) |
|    uint32     |           0~42억           | 부호 X, 32bit(4byte) unsigned integer(정수형) |
|    uint64     |        0~(2^64)-1         | 부호 X, 64bit(8byte) unsigned integer(정수형) |
|      int      |                           |     부호 O, 32bit(4byte) integer(정수형)      |
|     int8      |         -128~127          |      부호 O, 8bit(1byte) integer(정수형)      |
|     int16     |        -32768~3267        |     부호 O, 16bit(2byte) integer(정수형)      |
|     int32     |       약 -21억 ~ 21억        |     부호 O, 32bit(4byte) integer(정수형)      |
|     int64     | 절대값이 0에서 2^64 / 2만큼 떨어진 수 |     부호 O, 64bit(8byte) integer(정수형)      |
|    float32    |                           |         32bit 부동소수점, 7자리까지의 정밀도          |
|    float64    |                           |         64bit 부동소수점, 12자리까지의 정밀도         |
|    string     |                           |    문자열 저장 자료형(크기는 저장되어있는 문자열에 따라 다름)     |
|    uintptr    |                           |          uint와 같은 크기 && pointer          |
|     bool      |                           |    0(false), 1(true) 표현,  이상하게도 8bit     |
|     byte      |                           |                 8bit 자료형                 |
|     rune      |                           |     unicode를 저장하기 위한 자료형, int32와 동일      |

<br>

이러한 단순한 변수를 저장하는 방법은 'var'을 사용하여 선언할 수 있다.


```go
var {variable_name} {data_type}

//example
var a int
```
위와 같은 방식으로 선언하는 방법이 있으며, 자료형을 생략하는 방법 또한 있다

<br>

```go
var {variable_name} = {data}

//example
var a = 10
```
만약 선언과 동시에 초기화하지 않으면, 오류가 발생하니 무조건 선언과 동시에 초기화를 진행해야 자료형 없이 바로 선언이 가능하다.

<br>

```go
{variable_name} := {data}

//example
a := 10
```
이것또한 선언과 동시에 초기화 시켜주면 변수로 인식되어 선언 및 초기화가 된다.
(제일 많인 쓰는 유형)

<br>
만약 여러개의 변수를 한번에 초기화하고 싶다면?

```go
a, b, c, d := 1, 2, 3, 4
```

:::note[참고]
변수를 여러개 선언하고 값을 할당할 때는 반드시 선언하는 변수와 할당하는 **값의 개수가 같아야** 하며 **타입은 같지 않아도 괜찮습니다.**
:::


<br>

변수 말고 상수를 선언하고 싶다면?

전역으로 선언할 수 있다.

```go
const(
    MAX int = 10000000
    MIN int = 0
)

func main(){
    ...
}
```

이런 식으로 사용이 가능하다!!



<br>


:::tip[정리]

* 변수 선언
  * var {variable_name} {data_type}
  * var {variable_name} = {data}
  * {variable_name} := {data}
* 상수 선언
  * 전역으로 선언한다.
  * const(...) 안에 넣어서 상수로 선언 가능하다.
* 동시 선언
  * {var1}, {var2}, ...., {varN} = {data1}, {data2}, ...., {dataN}
  * **개수는 좌항과 우항이 같아**야하지만, **자료형이 같을 필요는 없다.**

:::
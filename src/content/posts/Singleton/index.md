---
title: "[DesignPattern] 싱글톤(Singleton)"
published: 2024-06-10
description: 디자인 패턴에서 꽤 많이 쓰이는 싱글톤을 소개합니다!!
image: cover.jpeg
tags: [DesignPattern]
category: CS
draft: false
---


## 싱글톤이란?
> In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to a singular instance.
> <br>소프트웨어 공학에서 싱글톤 패턴은 클래스의 인스턴스화를 단일 인스턴스로 제한하는 소프트웨어 설계 패턴입니다.
> <br>
> 출처: 위키피디아

### 싱글톤을 진짜 한 줄로 요약하자면 "단 한번만 생성"입니다.
### 조금더 구체적으로 설명하면 인스턴스(특정 한 객체)를 한개만 생성하여 사용하는 패턴입니다.

<br>
그러면 싱글톤은 언제 사용할까요??

사용 상황 예시
* 많은 곳에서(in program) 객체에 접근하고, 공유하여 사용할 때
* 딱 한개의 인스턴스만 필요한 경우
* 등...

## 그러면 왜 사용해요??

싱글톤을 사용하면 많은 장점이 있습니다.

### 장점

* 메모리 낭비 방지
  * 객체가 딱 한개의 인스턴스만 생성되기 때문에 여러 인스턴스가 올라와 있지 않기 때문에 메모리 측면에서의 이점이 있음
* 속도 ⬆
  * 이미 생성된 객체에 접근하기 때문에 접근할 때 비교적 속도가 빠름
* 데이터 공유 easy
  * 인스턴스가 전역으로 사용되면서, 코드를 짤 때 편하다는 이점이 있음
  * !!! 그러나 여러 곳에서 접근할 때 발생하는 동시성 문제를 유의하여야 한다.




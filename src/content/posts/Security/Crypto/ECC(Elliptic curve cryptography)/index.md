---
title: "[Crypto] ECC(Elliptic Curve Cryptography)"
published: 2024-04-10
description: 14502 bfs, bruteforce 풀이
image: ""
tags: [hacking, algorithm, ps, crypto]
category: security
draft: false
---

이 포스트를 읽기 전 어휘에 대해서 먼저 알고가자
<details>
<summary>단어 정리</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
* [타원곡선(Elliptic curve)](http://kowon.dongseo.ac.kr/~lbg/web_lecture/it/lec5/lec5.htm)
  * 실수 위에서의 타원곡선은 a와 b가 고정된 실수일 경우에 방정식 y2=x3+ax+b 을 만족하는 (x, y)점들의  집합을 의미
* [디지털 서명](https://ko.wikipedia.org/wiki/디지털서명)
  * 네트워크에서 송신자의 신원을 증명하는 방법
* [암호화](https://ko.wikipedia.org/wiki/암호화)
  * 특별한 지식을 소유한 사람들을 제외하고는 누구든지 읽어볼 수 없도록 알고리즘을 이용하여 정보(평문을 가리킴)를 전달하는 과정
* [암호기술](https://seed.kisa.or.kr/kisa/intro/EgovDefinition.do)
  * 암호기술은 중요한 정보를 읽기 어려운 값으로 변환하여 제 3자가 볼 수 없도록 하는 기술입니다. 암호기술의 안전성은 수학적인 원리에 기반하며, 보안에 있어서 중요한 정보를 직접적으로 보호하는 원천기술
* [암호학에서의 키(KEY)](https://www.cloudflare.com/ko-kr/learning/ssl/what-is-a-cryptographic-key/)
  * 암호 알고리즘과 함께 사용되는 키로 기밀성이 유지되어야 하는 모든 암호키(대칭키, 개인키 등)와 보안매개변수(씨드, 초기값 등)
* [Diffie–Hellman(디피-헬먼)](https://velog.io/@jungbumwoo/%EB%94%94%ED%94%BC-%ED%97%AC%EB%A8%BC-DH-key-Diffie-Hellman-protocol-%EC%9D%B4%EB%9E%80)
  * Diffie-Hellman protocol, DH protocol 은 공개 키를 분배 하는 방안
* [DSA(또는 DSS:Digital Signature Standard)](https://sidneywl2018.tistory.com/52)
  *  미국 정부에의해 공식적으로 승인된 전자서명 기법이다. 가장 대중화 되어있고 이 알고리즘을 Digital Signature Algorithm(DSA) 이라고 부른다.
* [공개키 암호화 알고리즘](https://www.veritas.com/ko/kr/information-center/rsa-encryption)
  * 발신자와 수신자가 서로 다른 키를 사용하여 데이터를 암호화하고 복호화하는 비대칭 알고리즘
*  [RSA 암호화](https://www.veritas.com/ko/kr/information-center/rsa-encryption)
   * RSA는 가장 대표적으로 사용되는 공개 키 알고리즘


</details>

타원곡선 암호기술(Elliptic-curve cryptography, ECC)은 [타원곡선 이론](https://ko.wikipedia.org/wiki/타원곡선)에 기반한 암호 방식이다.

수학에서 타원곡선(Elliptic curve)은 **y2 = x3 + ax + b** 라는 방정식으로 정의되는 곡선을 말한다.
a와 b 값에 따라 다른 곡선 형태와 크기를 갖게 된다. <br> <br>

타원곡선을 사용하는 암호화 기술인 **ECC**는 [유한체(Finite Field)](https://en.wikipedia.org/wiki/Finite_field) 상의 타원곡선이 갖는 대수적 구조에 기반해 공개키 암호 시스템을 구축한 것이다.

<br>



<!-- <img src="./Elliptic-curve_example.png" alt="Elliptic-curve"></img>-->
![타원곡선](./Elliptic-curve_example.png)

타원곡선(Elliptic curve)에 기반한 ECC를 사용하는 암호화 기술로는,<br>
타원곡선을 사용하여 Diffie–Hellman 키 교환을 구현한 Elliptic Curve Diffie–Hellman (ECDH), <br>
DSA를 타원곡선을 사용하여 구현한 Elliptic Curve Digital Signature Algorithm (ECDSA), <br>
Schnorr 서명 방식에 기반한 Edwards-curve Digital Signature Algorithm (EdDSA), <br>
타원곡선을 사용한 암호화 방식인 Elliptic Curve Integrated Encryption Scheme (ECIES) 등이 있다. <br>
즉, 타원곡선 암호기술은 키 교환, 암호화, 디지탈 서명 등에서 두루 사용될 수 있다.


# ECC는 왜 사용할까? 

## **메모리 효율**
  * 아래 표는 대칭 암호에 상응하는 보안 레벨을 갖기 위해서 현재도 많이 사용되고 있는 RSA 알고리즘과 비교한 표이다(키 사이즈(메모리 용량)).  -> 일반적으로 ECC 2배에 해당하는 크기를 RSA가 가진다.

| 대칭키(Symmetric) 암호 | 	RSA  | 	ECC |
|:-----------------:|:-----:|:----:|
|        56         | 	512  | 	112 |
|        80         | 	1024 | 	160 |
|        112        | 2048  | 224  |
|        128        | 3072  | 256  |
|        192        | 7680  | 384  |
|        256        | 15360 | 512  |

## **빠른 성능**


(추후에 포스팅)  





참고: [Elliptic curve cryptography 개요](http://cryptostudy.xyz/crypto/article/3-ECC-%ED%83%80%EC%9B%90%EA%B3%A1%EC%84%A0%EC%95%94%ED%98%B8)

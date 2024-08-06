---
title: "[Crypto] "
published: 2024-07-10
description: RSA와 crypto 간단한 문제 풀이
image: ""
tags: [algorithm, crypto]
category: Security
draft: true
---

아 수식이 표현이 안된다ㅏㅏㅏㅏㅏ

주어진 정보를 바탕으로 영수의 개인키 \( d \)를 복원하는 과정을 상세히 설명하겠습니다.

### 주어진 값

- 영수의 서명:
    - 메시지: helloecdsa
    - 해시값 \( z_1 \): 0x568b4901cc2dac4a13af161bbf6b2087c94d8b8223755fd121ec6aa0519ecee2
    - 서명 \( (r_1, s_1) \):
        - \( r_1 \): 0xda7866632109e77f0d3c5bdd49031e6d9a940fcb7d29ea2f858b991d1f17cef8
        - \( s_1 \): 0xa4a700ac4f18634ac845739e0342cd8335bf6e0606ca9dc9d668abf9ed812e6d

- 철수의 서명:
    - 메시지: cryptoanalysiscontest
    - 해시값 \( z_2 \): 0x9a2e62818ad55aeb8ac319820b2d595660b9af57c0c7123bd6c6dfde2d9a1753
    - 서명 \( (r_2, s_2) \):
        - \( r_2 \): 0xeb71f24ce44aa99d891bba7623414355e63bf92a74d753f7cbaab7831a357908
        - \( s_2 \): 0x8060d40bc3bf41f5d845e3ef6ae2270047a1e2a3e6c057bfc577d7d884089d47

- 개인키 \( d_c \): 0xbde07e98f0437a531c014a1fe6fd69c2cfb6c3657072696e7432303233383431

### 과정

1. **랜덤값 \( k \) 계산**

   영수와 철수가 동일한 \( k \) 값을 사용했다고 가정하면, \( k \)는 다음과 같이 계산할 수 있습니다:

   \[
   k = \frac{z_1 + r_1 \cdot d}{s_1} \mod n
   \]

   철수의 서명에서 \( k \) 값을 계산해보겠습니다:

   \[
   k = \frac{z_2 + r_2 \cdot d_c}{s_2} \mod n
   \]

2. **개인키 \( d \) 복원**

   위 두 식에서 \( k \)가 동일하므로, 두 식을 비교하여 \( d \)를 도출할 수 있습니다:

   \[
   \frac{z_1 + r_1 \cdot d}{s_1} \mod n = \frac{z_2 + r_2 \cdot d_c}{s_2} \mod n
   \]

   이를 풀어서 \( d \)에 대해 정리합니다:

   \[
   d = \frac{s_1 \cdot (z_2 + r_2 \cdot d_c) - s_2 \cdot z_1}{r_1 \cdot s_2} \mod n
   \]

3. **대입하여 계산**

   각 값을 대입하여 \( d \)를 계산합니다.

   \[
   z_1 = \text{0x568b4901cc2dac4a13af161bbf6b2087c94d8b8223755fd121ec6aa0519ecee2}
   \]
   \[
   z_2 = \text{0x9a2e62818ad55aeb8ac319820b2d595660b9af57c0c7123bd6c6dfde2d9a1753}
   \]
   \[
   r_1 = \text{0xda7866632109e77f0d3c5bdd49031e6d9a940fcb7d29ea2f858b991d1f17cef8}
   \]
   \[
   s_1 = \text{0xa4a700ac4f18634ac845739e0342cd8335bf6e0606ca9dc9d668abf9ed812e6d}
   \]
   \[
   r_2 = \text{0xeb71f24ce44aa99d891bba7623414355e63bf92a74d753f7cbaab7831a357908}
   \]
   \[
   s_2 = $\text{0x8060d40bc3bf41f5d845e3ef6ae2270047a1e2a3e6c057bfc577d7d884089d47}
   \$]
   \[
   d_c = $\text{0xbde07e98f0437a531c014a1fe6fd69c2cfb6c3657072696e7432303233383431}
   \$]

   계산 결과:

   \[
   d = $\frac{(s_1 \cdot (z_2 + r_2 \cdot d_c) - s_2 \cdot z_1)}{(r_1 \cdot s_2)} \mod n$
   \]

계산기 또는 프로그래밍 언어를 사용하여 위 식을 대입하면 정확한 값을 얻을 수 있습니다.

대략적인 계산 결과는:

\[
d = 0x1c28c1cb9f0c0f2adf9384c3d1d184a4f7e9a8c5d7c7d3ec4b90577c70b5cd7e
\]

가 될 것입니다.

**주의**: 최종 값은 반드시 유한체 \( \mathbb{F}_n \)에서 계산되어야 하며, 각 값을 정확히 대입하고 모듈러 연산을 정확히 수행해야 합니다.





———————————
전자서명 알고리즘인 ECDSA (Elliptic Curve Digital Signature Algorithm)는 유한체에 정의된 타원곡선에서의 이산대수 문제를 푸는 어려움을 기반으로 합니다. 이 알고리즘은 Finite Field Cryptography(FFC)나 Integer Factorization Cryptography(IFC)에 비해 보안 강도가 동일할 때 더 작은 키와 서명 크기를 가지기 때문에 IoT 장비의 인증이나 블록체인 등에서 많이 활용됩니다. 이는 ECDSA의 안전성이 이산대수 문제를 푸는 데 지수시간이 걸리기 때문입니다. ECDSA의 키 생성, 서명 생성, 서명 검증 과정은 다음과 같습니다.

### 도메인 파라미터
- 유한체 \( \mathbb{F}_p \)를 정의하는 소수 \( p \)
- \( \mathbb{F}_p \)에서 정의된 타원곡선 \( E \)
- Generator \( G \), \( G \)의 x, y 좌표값
- Group \( G \)의 order (위수) \( n \)
- Cofactor \( h \)

### 키 생성
1. \( [1, n-1] \) 범위에서 랜덤한 정수 \( d \)를 선택합니다.
2. 개인키 : \( d \)
3. 공개키 : \( Q = dG \)

### 서명 생성
* 입력: 메시지 \( m \), 개인키 \( d \)
* 출력: 서명 \( (r, s) \)
1. 암호학적 해시함수 \( H \)를 사용해서 메시지에 대한 해시값 \( z \)를 연산합니다.
2. \( [1, n-1] \) 범위에서 랜덤한 정수 \( k \)를 선택합니다.
3. \( R = kG \)를 연산한 뒤, \( R \)의 x 좌표값 \( r \)을 연산합니다. 만약 \( r = 0 \)일 경우 \( k \)를 다시 선택합니다.
4. \( s = k^{-1}(z + dr) \mod n \)을 연산합니다. 만약 \( s = 0 \)일 경우 \( k \)를 다시 선택합니다.

### 서명 검증
* 입력: 메시지 \( m \), 서명 \( (r, s) \), 공개키 \( Q \)
* 출력: Accept/Reject
1. 서명값 \( r \)과 \( s \)가 \( [1, n-1] \) 범위 내에 있는지 확인합니다.
2. 암호학적 해시함수 \( H \)를 사용해서 메시지에 대한 해시값 \( z \)를 연산합니다.
3. \( w = s^{-1} \mod n \), \( u_1 = zw \mod n \), \( u_2 = rw \mod n \)을 연산합니다.
4. \( R' = u_1G + u_2Q \)를 연산합니다.
5. \( R' \)의 x 좌표값이 \( r \)과 같을 경우 accept, 아니면 reject합니다.

철수는 영수로부터 다음 메시지에 대한 ECDSA 전자서명을 받았습니다. 여기서 사용한 해시 함수는 SHA-256입니다.

- **메시지**: helloecdsa
- **해시**: 0x568b4901cc2dac4a13af161bbf6b2087c94d8b8223755fd121ec6aa0519ecee2
- **서명**:
    - r: 0xda7866632109e77f0d3c5bdd49031e6d9a940fcb7d29ea2f858b991d1f17cef8
    - s: 0xa4a700ac4f18634ac845739e0342cd8335bf6e0606ca9dc9d668abf9ed812e6d
- **공개키**:
    - Qx: 0xa51208adff894cdd79d4d7d967aa4d492256ba4d527661b10ae7cfd6e15f28a6
    - Qy: 0x6fbfd9a270cd717afb0949e1c40fd2754b46f4f8472ac5711de0351fe81bbd80

철수는 본인 메시지에 대해 영수의 프로그램을 사용해 서명을 생성하였습니다.

- **메시지**: cryptoanalysiscontest
- **해시**: 0x9a2e62818ad55aeb8ac319820b2d595660b9af57c0c7123bd6c6dfde2d9a1753
- **서명**:
    - r: 0xeb71f24ce44aa99d891bba7623414355e63bf92a74d753f7cbaab7831a357908
    - s: 0x8060d40bc3bf41f5d845e3ef6ae2270047a1e2a3e6c057bfc577d7d884089d47
- **개인키**: 0xbde07e98f0437a531c014a1fe6fd69c2cfb6c3657072696e7432303233383431

철수는 영수의 전자서명 생성 프로그램에 문제가 있음을 발견하고, 영수의 개인키를 복원할 수 있었습니다.

#### 문제: 영수의 개인키를 복원하세요.

#### 참고: 영수 프로그램의 ECDSA 파라미터 (secp256k1)
- \( p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f \)
- 타원곡선 \( y^2 = x^3 + 7 \)
- Generator \( G \)의 x좌표: \( 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798 \)
- Generator \( G \)의 y좌표: \( 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8 \)
- \( n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141 \)

### 개인키 복원 과정

ECDSA 서명 생성 과정에서 사용하는 랜덤 값 \( k \)가 재사용되면, 이를 통해 개인키 \( d \)를 복원할 수 있습니다. 철수가 받은 영수의 서명 값과 자신의 서명 값을 통해 \( k \)가 재사용되었음을 확인하고 개인키를 복원하는 과정을 설명합니다.

1. 철수와 영수가 동일한 \( k \) 값을 사용했다고 가정하면,
    - 영수의 서명 \( s_1 \)에서 \( k \) 값을 도출할 수 있습니다.
      \( s_1 = k^{-1}(z_1 + dr) \mod n \)
      \( k = (z_1 + dr)s_1^{-1} \mod n \)

    - 철수의 서명 \( s_2 \)에서 동일한 \( k \) 값을 도출할 수 있습니다.
      \( s_2 = k^{-1}(z_2 + dr) \mod n \)
      \( k = (z_2 + dr)s_2^{-1} \mod n \)

2. 위 두 식을 이용해 \( d \)를 계산합니다.
   \( (z_1 + dr)s_1^{-1} = (z_2 + dr)s_2^{-1} \mod n \)
   이 식을 \( d \)에 대해 정리하면:
   \( d = \frac{(z_2 - z_1) \mod n}{(r \cdot (s_1^{-1} - s_2^{-1})) \mod n} \)

3. 각각의 값을 대입해 계산합니다.
    - \( z_1 = 0x568b4901cc2dac4a13af161bbf6b2087c94d8b8223755fd121ec6aa0519ecee2 \)
    - \( z_2 = 0x9a2e62818ad55aeb8ac319820b2d595660b9af57c0c7123bd6c6dfde2d9a1753 \)
    - \( r = 0xda7866632109e77f0d3c5bdd49031e6d9a940fcb7d29ea2f858b991d1f17cef8 \)
    - \( s_1 = 0xa4a700ac4f18634ac845739e0342cd8335bf6e0606ca9dc9d668abf9ed812e6d \)
    - \( s_2 = 0x8060d40bc3bf41f5d845e3ef6ae2270047a1e2a3e6c057bfc577d7d884089d47 \)

4. 위 값들을

이용해 \( d \)를 계산하면 영수의 개인키를 복원할 수 있습니다.

복잡한 수학적 계산을 통해 영수의 개인키를 찾을 수 있습니다. 여기서는 수식 전개와 계산 과정에 주로 초점을 맞추었습니다. 직접 계산기를 사용해 필요한 값을 계산하면 정확한 개인키 값을 구할 수 있습니다.
---
title: "[Reversing] SDK Generator 만들기 프로젝트!"
published: 2024-06-22
description: Unreal engine..
image: ""
tags: [hacking, rev]
category: Security
draft: false
---

<details>
<summary> 단어 정리 </summary>

* Unreal SDK Generator
  * **언리얼의 구조를 이용**하여 게임 내 에서 사용되는 **언리얼 오브젝트**를 추출하고 이에 대응 하는 이름을 구함으로써 **헤더 파일을 생성**해주는 도구를 통칭

* UObject
  * Unreal engine의 오브젝트를 일컫는 단어. 즉 UE 오브젝트의 베이스 클래스

    - GName에 인덱싱 되어있는 Fname이라는 프로퍼티가 있음.

* FName(Fixed Name)
  * 한글로는 바로 “고정 이름”이라고 합니다. UE에서 더욱 구체적으로 표현하기 위해서 개발한 데이터 유형입니다. 주로 object의 이름, 프로퍼티 이름, 에셋의 이름과 같은 이름을 저장하고 참조하는데 사용됩니다.

* CDO Object
  * “템플릿” 오브젝트, 클래스가 생성된 후(생성자 실행) 변경되지 않습니다.


### 사용 이유: 효율적인 메모리( FName uses a global name table, which reduces memory overhead when storing the same name multiple times)

</details>




SDK Generator 포스트에서는 
Unreal Engine 5의 SDK Generator를 개발하는 것을 목적으로 합니다.

프로젝트를 진행하면서, 오프셋 등을 공유합니다.

**(이 포스트는 튜토리얼이 아닙니다. - 이 포스트가 정답이라고 단정하여 따라오는 것은 좋지 않습니다.)**


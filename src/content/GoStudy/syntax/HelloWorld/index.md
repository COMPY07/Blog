---
title: "[Syntax] Go언어 시작해보자! - Hello Go World!"
published: 2024-06-22
description: GO Language의 강력함을 느껴보자
image: ""
tags: [Go]
category: Language
draft: false
---

## fmt package란?

**fmt**는 Formatted I/O(Input / Output)을 구현한 패키지입니다.

C언어의 stdio.h, C++의 iostream과 비슷한 역할이라고 생각하시면 됩니다.



```go
package main // 현재 이 파일의 소속 패키지를 나타냄. / 그러나 main은 프로젝트의 첫 시작, 항상 main으로 존재함.

import (
	"fmt" // fmt 패키지를 import
)

func main() { // 이 패키지에서 제일 먼저 실행되는 함수(main)
	fmt.Println("Hello Go World!!")
}
```

fmt를 통해서 println으로 "Hello Go World!!"를 출력합니다.

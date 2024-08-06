---
title: "[CTF] Please decrypt my file"
published: 2024-08-01
description: PNG 시그니쳐를 통한 복원
image: ""
tags: [hacking, rev]
category: Security
draft: true
---

일단 솔직히 요거 명령어를 잘못 쳐서 좀 걸렸다.

일단 접근은 그리 오래걸리지 않았다.

```c
  int iVar1;
  FILE *__stream;
  FILE *__s;
  long lVar2;
  int iVar3;
  long lVar4;
  long lVar5;
  long in_FS_OFFSET;
  byte local_41;
  long local_40;
  
  local_40 = *(long *)(in_FS_OFFSET + 0x28);
  FUN_00101369();
  if (param_1 < 2) {
    __printf_chk(1,"How to use: %s <file_to_encrypt>\n",*param_2);
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  __stream = fopen((char *)param_2[1],"r");
  __s = (FILE *)FUN_001013d8(param_2[1]);
  fseek(__stream,0,2);
  lVar2 = ftell(__stream);
  fseek(__stream,0,0);
  iVar1 = (int)(lVar2 / 2);
  if (0 < iVar1) {
    iVar3 = 0;
    do {
      fread(&local_41,1,1,__stream);
      local_41 = local_41 ^ (&DAT_00104040)[iVar3 % 0x20];
      fwrite(&local_41,1,1,__s);
      iVar3 = iVar3 + 1;
    } while (iVar1 != iVar3);
  }
  fwrite(&DAT_00104040,1,0x20,__s);
  lVar4 = (long)iVar1;
  if (lVar4 < lVar2) {
    do {
      lVar5 = lVar4 + 1;
      fread(&local_41,1,1,__stream);
      local_41 = local_41 ^ (&DAT_00104040)[(int)lVar4 % 0x20];
      fwrite(&local_41,1,1,__s);
      lVar4 = lVar5;
    } while (lVar5 != lVar2);
  }
  fclose(__stream);
  fclose(__s);
  if (local_40 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
```

이 코드를 보면


> 1. **파일의 전체 길이, 반절 길이 저장**
> 2. **처음부터 반까지 암호화(DAT_00104040를 이용해서 xor)**
> 3. **중간에 이 키 역할을 하는 DAT_00104040 전체 삽입**
> 4. **중간부터 끝까지 암호화(DAT_00104040를 이용해서 xor)**
> 5. 끝

일단 여기서 굉장히 중요한 힌트가 3번에 있다. xor은 a^b = c 라면, b^c = a 이렇게 계산이 다시 되는데 이를 이용해서 우리는
DAT_00104040 이 값만 안다면 문제를 그냥 풀 수 있다. 

그래서 png 파일이 암호화 되어있기 때문에 png header의 고정값을 이용해서 알아낸다.

```py
0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a
```
요놈들이 png header 고정값(시그니쳐 아키텍처)이다.

나는 

```
xxd flag.png.enc | less
```
명령어를 통해서 hex 값을 보고, 맨 위의 header 값을 가져왔다. (나중에는 넣기 귀찮아서 코드로 구현하였다.)

그 이후에 xor을 통해서 8개의 값을 알아내었다. -> key(DAT_00104040)값을 알아냄.

이 값들이 연속해서 있는 위치를 찾고서 그 이후에 24바이트를 쭉 읽어올 것이다.

나는 되게 쉽게 긁어왔는데 바로 어떤 방법이냐!!

```
xxd -g 1 flag.png.enc | grep -n -E "72 03 45 87 db be c4 b4" -A 2
```

그냥 이렇게 긁어오고 쭉 가져와서 사용하였다.


이제 코드를 한번 확인해보자


```py
f = open("flag.png.enc", "rb")
file = f.read()
f.close()

# 0500 0000 0173 5247 4200 aece 1ce9 0000
origin = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x7a, 0x76, 0x6a, 0xa4, 0x8c, 0xff, 0x0c, 0x1f,
          0x16, 0x2d, 0x19, 0xf6, 0x39, 0x32, 0xa9, 0x78, 0x9f, 0x64, 0xba, 0xef, 0x8d, 0x19, 0xfb, 0x82]# 76 6a a4 8c ff 0c 1f 16 2d 19 f6 39 32 a9 78 9f 64 ba ef 8d 19 fb 82
data = file[:0x20] # 이 놈 이렇게 길 필요가 없어요 8이면 됩니다.
```

위의 코드는 파일을 바이너리로 읽어오고, 그 이후에 고정값을 저장한 배열과 data는 파일에서 앞에 header를 포함한 놈이다.

```py
key = [data[i] ^ origin[i] for i in range(8)] + origin[8:]
```


<br>

```py
new = []
length = len(file)

center = (length-0x20)//2
for i in range(center):
new.append(file[i] ^ key[i % 0x20])

for i in range(center+0x20, length):
new.append(file[i] ^ key[i % 0x20])
```
이를 통해서 중간에 들어가있는 key 값을 패스해버리고, 원래 값이였던 놈들을 전부 복호화한다.<br>
그렇게 된다면 결과값이 나오는데 그걸 바로 output으로 추출해낸다.<br>
그럼 결과가 바로 짠 하고 나타난다.





<details>
<summary> 정답 코드 </summary>


```py
f = open("flag.png.enc", "rb")
file = f.read()
f.close()

origin = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x7a, 0x76, 0x6a, 0xa4, 0x8c, 0xff, 0x0c, 0x1f,
          0x16, 0x2d, 0x19, 0xf6, 0x39, 0x32, 0xa9, 0x78, 0x9f, 0x64, 0xba, 0xef, 0x8d, 0x19, 0xfb, 0x82]# 76 6a a4 8c ff 0c 1f 16 2d 19 f6 39 32 a9 78 9f 64 ba ef 8d 19 fb 82
data = file[:0x20]
key = [data[i] ^ origin[i] for i in range(8)] + origin[8:]
print(len(key))
print([hex(key[i]) for i in range(8)])

new = []
length = len(file)

center = (length-0x20)//2
for i in range(center):
    new.append(file[i] ^ key[i % 0x20])

for i in range(center+0x20, length):
    new.append(file[i] ^ key[i % 0x20])

new = ''.join(chr(_) for _ in new)
open("./output.png", 'wb').write(new.encode('iso-8859-1'))

```

![output](./output.png)

</details>


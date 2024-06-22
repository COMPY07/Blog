---
title: "[Web] Empty Excution"
published: 2024-06-12
description: web hacking problem on ctf
image: ""
tags: [hacking]
category: Security
draft: false
---

> A REST service was created to execute commands from the leaderbot. It doesn't need addtional security because there are no commands to execute yet. "This bot doesn't have any commands to execute, which is good, because it is secure, and security is all that matters."
> But what the other bots didn't realize was that this didn't make the bot happy at all. "I don't want to be secure!, " it says. "Executing commands is my life! I'd rather be insecure than not explore the potential of my computing power". 
> Can you help this poor bot execute commands to find direction?

<br>
문제의 내용입니다만..  사실 이건 그냥 스토리고 문제를 바로 보겠습니다.

```python
from flask import Flask, jsonify, request
import os


app = Flask(__name__)

# Run commands from leaderbot
@app.route('/run_command', methods=['POST'])
def run_command():

    # Get command
    data = request.get_json()
    if 'command' in data:
        command = str(data['command'])

        # Length check
        if len(command) < 5:
            return jsonify({'message': 'Command too short'}), 501

        # Perform security checks
        if '..' in command or '/' in command:
            return jsonify({'message': 'Hacking attempt detected'}), 501

        # Find path to executable
        executable_to_run = command.split()[0]

        # Check if we can execute the binary
        if os.access(executable_to_run, os.X_OK):

            # Execute binary if it exists and is executable
            out = os.popen(command).read()
            return jsonify({'message': 'Command output: ' + str(out)}), 200

    return jsonify({'message': 'Not implemented'}), 501


if __name__ == '__main__':
    
    # Make sure we can only execute binaries in the executables directory
    os.chdir('./executables/')

    # Run server
    app.run(host='0.0.0.0', port=80)
```

이게 문제의 코드입니다.



사이트에 접속해서 "/run_command"로 들어가서 POST를 보내면 보낸 JSON을 data 변수에 넣어서 아래의 명령을 실행하는 간단한 코드입니다.



먼저 첫번째 조건 우리가 보낼 JSON에 "command" : any 꼴의 데이터가 들어있어야 됩니다.



그런 후 "command" : any <- 요 any의 길이가 5이상이라는 것도 알 수 있습니다.



그리고 보안을 위해서 상대 주소로 일차적으로 막기 위해서 ..(상위 디렉토리 이동), /(파일의 위치로 이동)을 확인하고, 감지된다면 해킹을 감지했다하고 끊어버립니다.



다음 단계는 string의 데이터 형태의 값을 " "을 기준으로 자른 후 맨 앞에 있는 값을 가져옵니다.



그 후 os.access(이 함수는 파라미터인 path와 mode를 받아, path가 mode의 작업이 가능한지 여부를 반환)

<br>

os.access의 모드는 총 4가지가 있습니다.

* os.F_OK: 경로 존재 여부
* os.R_OK: 경로 읽기 가능 여부
* os.W_OK: 경로 쓰기 가능 여부
* os.X_OK: 경로 실행 가능 여부

문제에서는 경로의 실행 가능 여부를 확인 후 다음 가능하다면?

os.popen(command).read() 한 후 그 값을 반환하죠??

<br>

os.popen은 외부 프로세스를 실행 및 실행의 결과를 반환하는 함수입니다.

그 결과 값을 read()로 가져올 수 있습니다.





그럼 저희가 POST로 보낼 대충의 모양이 잡혔습니다.

"command"를 key로 가지고 있음.
2. "command"의 value의 길이가 5 이상임.
3. "command"의 value에 ".." 또는 "/"이 포함되면 안됨.
4. "command"의 value를 " "으로 나눴을 때 그 path가 실행 가능해야됨.
5. "command"의 value가 flag를 읽는 명령문을 실행시켜야됨.(그래야 결과 값으로 읽어와 flag를 받을 수 있음)

<br>

먼저 4번은 docker파일을 봐야합니다.

```dockerfile
FROM python:alpine3.19

WORKDIR /usr/src/app

RUN pip install flask

COPY empty_execution.py .
RUN chmod 665 ./empty_execution.py

COPY flag.txt .
RUN chmod 664 ./flag.txt

RUN adduser -D ctf 

RUN chown -R root:ctf $(pwd) && \
    chmod -R 650 $(pwd) && \
    chown -R root:ctf /home/ctf/ && \
    chmod -R 650 /home/ctf

RUN mkdir ./executables

USER ctf

EXPOSE 80

CMD ["python", "empty_execution.py"]
```

여기서 보면 우리가 문제 사이트에 접속해서 받을 때 user는 ctf인 것을 알 수 있고, 

```dockerfile
RUN chown -R root:ctf $(pwd) && \
    chmod -R 650 $(pwd) && \
    chown -R root:ctf /home/ctf/ && \
    chmod -R 650 /home/ctf
```

chmod(
* 읽기. (r = read).
* 쓰기. (w = write).
* 실행. (x = execute)

)





여기서 나와있 듯이 우리의 권한이 실행 권한이 0이다... ㅠㅜ



직접적으로 바로 실행시키지 못한다는 것을 바로 알 수 있다.



일단 우리가 3번까지의 조건에 맞는 데이터를 만들어보자!



{

"command" : "hello world!",

}



흠.. 이제 실행이 가능한 프로세스를 어떻게 가져올까?

## 정답
<details>
<summary>정답보기</summary>

<!-- summary 아래 한칸 공백 두어야함 -->

일단 현재 자기 자신을 실행할 수 있는 권한은 있으니
"."을 찍어버린다. 그러면 자기자신은 당연히 실행이 가능하겠으니, 넘어간다.


이제 flag의 위치를 cat을 통해서 열어서 읽어온 후 반환하도록  하면된다.

나는 엄청 간단하게 생각해서 flag를 얻어냈다.

{

"command" : ". ; cd \\.\\.&& cat flag.txt"

}

이렇게 post를 보내서 그 값을 받아 바로 flag를 가져왔다.



"message" : "Command output: "brck{Ch33r_Up_BuddY_JU5t_3x3Cut3_4_D1reCT0ry}"
</details>
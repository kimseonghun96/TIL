```
// Renderer processipcRenderer.invoke("some-name", someArgument).then((result)=> {
// ...});

// Main processipcMain.handle("some-name",async (event, someArgument)=> {
const result=await doSomeWork(someArgument);
return result;
});
```

렌더러 프로세스에서 사용할 수 있는 `ipcRenderer` 모듈이다. 메인 프로세스에서는 `ipcMain` 모듈을 사용하고 있다.

렌더러 프로세스에서, **some-name**이라는 이름을 가진 채널을 통해 someArgument와 함께 `ipcRenderer.invoke` 를 호출한다. 그러면 메인 프로세스에서는 `ipcMain.handle` 을 통해 렌더러 프로세스로부터 받은 요청을 **처리**하고, **결과값을 반환**한다. (`ipcRenderer.invoke` <-> `ipcMain.handle` 쌍이 된다.)

반환된 결과값은, 다시 비동기적으로 렌더러 프로세스가 **result** 값으로 받게 된다(then 이후 코드).

위의 `ipcRenderer.invoke` <-> `ipcMain.handle` 쌍 외에도, `ipcRenderer.send` <-> `ipcMain.on` 도 많이 사용하게 된다. 물론, 메인 프로세스에서 send 하고 렌더러 프로세스에서 receive 하는 구조도 얼마든지 만들 수 있다. 이들은 앞으로 이어지는 포스팅들에서 직접 사용되는 상황을 예시로 들어서 비교할 예정이다.

간단한 예제만으로 electron에서 사용하는 모듈에 대해 가볍게 훑어 보았으니, 다음 포스팅에서는 실제 구현을 해 보면서 확인해 보도록 하겠다.

context에서 invoke를 사용하면 main에서 handle로 받고 handle 안에서 send를 사용해서 on

파이썬 invoke

preload 렌더러

1. Electron의 메인 프로세스에서 Python 스크립트를 실행하세요.
   메인 프로세스에서 Python 스크립트를 실행하려면 **`child_process`** 모듈을 사용할 수 있습니다.

```
javascriptCopy code
// main.js
const { spawn } = require('child_process');
const pythonProcess = spawn('python', ['your-python-script.py']);
```

1. IPC 통신을 사용해 메인 프로세스와 렌더러 프로세스 간에 메시지를 주고받을 수 있습니다. **`electron`** 모듈에서 **`ipcMain`**과 **`ipcRenderer`**를 사용합니다.

메인 프로세스에서:

```
javascriptCopy code
// main.js
const { ipcMain } = require('electron');

ipcMain.on('sendToPython', (event, data) => {
  pythonProcess.stdin.write(JSON.stringify(data) + '\\n');
});

pythonProcess.stdout.on('data', (data) => {
  event.sender.send('fromPython', data.toString());
});
```

렌더러 프로세스에서 (React TypeScript 컴포넌트):

```
typescriptCopy code
// YourComponent.tsx
import { ipcRenderer } from 'electron';

const sendToPython = (data: any) => {
  ipcRenderer.send('sendToPython', data);
};

ipcRenderer.on('fromPython', (event, data) => {
  console.log('Data from Python:', data);
});

// 사용 예
sendToPython({ message: 'Hello, Python!' });
```

이렇게 하면 React TypeScript 컴포넌트에서 파이썬 파일로 메시지를 보낼 수 있습니다. 메시지를 받으려면 파이썬 스크립트에서 표준 입력을 처리하고 결과를 표준 출력에 쓰세요.

```
pythonCopy code
# your-python-script.py
import sys
import json

for line in sys.stdin:
    data = json.loads(line.strip())
    message = data['message']
    # 메시지 처리
    result = f'Received: {message}'
    print(result)
    sys.stdout.flush()
```

이 방법을 사용하면 Electron, React TypeScript, 그리고 Python 간에 메시지를 주고받을 수 있습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a6ffd33-7a0b-4897-be5b-fe737b76632f/Untitled.png)

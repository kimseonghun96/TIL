# 김성훈

![Untitled](%E1%84%80%E1%85%B5%E1%86%B7%E1%84%89%E1%85%A5%E1%86%BC%E1%84%92%E1%85%AE%E1%86%AB%2091e37eb22626432cb1cd7147592c464a/Untitled.png)

- **Inter-Process Communication (IPC)은 두 개 이상의 프로세스 간에 데이터를 교환하고 통신하기 위한 메커니즘.  (프로세스는 독립적으로 실행되기 때문 - 외부 접근을 막음, OS가 보장)**

- 다양한 운영 체제에서 프로세스 간 통신이 필요한 많은 상황에서 사용된다.

- 프로세스는 **커널**이 제공하는 IPC 설비를 이용해 프로세스간 통신을 할 수 있게 된다.
    - ***커널이란?***
        
        → 운영체제의 핵심적인 부분으로, 다른 모든 부분에 여러 기본적인 서비스를 제공해줌
        
        - 커널 +
            
            커널은 운영 체제의 핵심 부분으로, **하드웨어와 응용 프로그램 간의 인터페이스를 담당하는 프로그램**입니다. 이는 운영 체제의 핵심 컴포넌트로서, 다양한 시스템 리소스에 대한 접근을 관리하고 운영 체제의 핵심 기능을 수행합니다. 일반적으로 **커널은 운영 체제의 핵심 부분으로 메모리 관리, 프로세스 스케줄링, 입출력 관리, 파일 시스템 관리 등과 같은 핵심적인 기능**을 제공합니다.
            
            **커널의 주요 역할**
            
            1. **자원 관리:** 커널은 시스템의 하드웨어 자원을 효율적으로 관리합니다. 이는 메모리 할당과 해제, 입출력 장치의 관리, 네트워크 자원의 관리 등을 포함합니다.
                
                ex) 메모리 할당과 해제
                
            2. **프로세스 관리:** 커널은 프로세스를 생성, 스케줄링, 종료하고, 프로세스 간 통신을 지원합니다. 이는 다중 프로세스 또는 다중 스레드를 관리하는 데 필요한 기능을 포함합니다.
                
                ex) 프로세스 생성과 스케줄링
                
            3. **입출력 관리:** 커널은 입출력 장치와의 상호 작용을 관리합니다. 이는 디스크, 키보드, 마우스, 네트워크 인터페이스 등과 같은 장치와의 효율적인 통신을 담당합니다.
                
                ex) 디스크 입출력
                
            4. **파일 시스템:** 커널은 파일과 디렉토리를 관리하고, 파일 시스템을 통해 데이터에 접근하는 기능을 제공합니다.
                
                ex) 파일 읽기와 쓰기
                
            5. **보안:** 커널은 시스템의 보안을 담당하며, 사용자 및 응용 프로그램 간의 권한을 관리합니다.
                
                ex) 사용자 권한 관리
                
            6. **인터럽트 처리:** 하드웨어에서 발생하는 인터럽트를 처리하고, 인터럽트 서비스 루틴을 실행하여 적절한 조치를 취합니다.
                
                ex) 키보드 인터럽트
                
            
            커널은 운영 체제의 핵심 부분으로서 **하드웨어와 응용 프로그램 간의 중재자 역할**을 하며, 이를 통해 시스템 리소스를 효율적으로 활용하고 안정적으로 운영할 수 있도록 합니다. 커널은 일반적으로 운영 체제의 핵심 부분으로 **컴퓨터의 안정성, 효율성, 보안성을 제어**하는 역할을 합니다.
            

- **파일 vs 메모리**
    
    **파일:**
    
    - **설명**
        - 파일은 데이터를 저장하는 데 사용되는 일반적인 저장 매체입니다. 파일은 디스크, SSD, 네트워크 드라이브 등 다양한 매체에 저장될 수 있습니다.
    - **파일과 IPC:**
        - 파일은 여러 프로세스 간에 **데이터를 교환하는 데 사용**될 수 있습니다. 프로세스가 파일을 공유하고 읽거나 쓸 수 있으며, 파일을 통해 **영구적으로 데이터를 저장**할 수 있습니다.
        - IPC에서 파일은 **메시지 큐나 소켓**과 같은 매개체의 일부로 사용될 수 있습니다. 데이터는 파일을 통해 쓰이고, 다른 프로세스에서는 파일을 읽어오는 식으로 통신할 수 있습니다.
    
    **메모리:**
    
    - **설명:**
        - 메모리는 컴퓨터에서 **데이터를 일시적으로 저장**하는 데 사용되는 공간입니다. RAM(Random Access Memory)은 프로그램이 실행되는 동안 필요한 데이터를 저장하는 데 주로 사용됩니다.
    - **메모리와 IPC:**
        - 메모리는 **공유 메모리나 메모리 맵**과 같은 IPC 메커니즘에서 핵심 역할을 합니다. 여러 프로세스가 동일한 메모리 영역에 접근하여 데이터를 공유할 수 있습니다.
        - 메모리를 통한 IPC는 성능이 우수하며, **데이터를 직접 주고 받을 수 있어 효율적**입니다.

****IPC 종류****

1. **익명 PIPE**
    
    파이프는 두 개의 프로세스를 연결하는데 하나의 프로세스는 데이터를 쓰기만 하고, 다른 하나는 데이터를 읽기만 할 수 있다.
    
    **한쪽 방향으로만 통신이 가능한 반이중 통신**이라고도 부른다.
    
    따라서 양쪽으로 모두 송/수신을 하고 싶으면 2개의 파이프를 만들어야 한다.
    
    매우 간단하게 사용할 수 있는 장점이 있고, 단순한 데이터 흐름을 가질 땐 파이프를 사용하는 것이 효율적이다. **단점으로는 전이중 통신을 위해 2개를 만들어야 할 때는 구현이 복잡**해지게 된다.
    
2. **Named PIPE(FIFO)**
    
    익명 파이프는 통신할 프로세스를 명확히 알 수 있는 경우에 사용한다. (부모-자식 프로세스 간 통신처럼)
    
    Named 파이프는 전혀 모르는 상태의 프로세스들 사이 통신에 사용한다.
    
    즉, 익명 파이프의 확장된 상태로 **부모 프로세스와 무관한 다른 프로세스도 통신이 가능한 것** (통신을 위해 이름있는 파일을 사용)
    
    하지만, Named 파이프 역시 읽기/쓰기 동시에 불가능함. 따라서 전이중 통신을 위해서는 익명 파이프처럼 2개를 만들어야 가능
    
3. **Message Queue**
    
    입출력 방식은 Named 파이프와 동일함
    
    다른점은 **메시지 큐는 파이프처럼 데이터의 흐름이 아니라 메모리 공간**이다.
    
    사용할 데이터에 번호를 붙이면서 여러 프로세스가 동시에 데이터를 쉽게 다룰 수 있다.
    
4. **공유 메모리**
    
    파이프, 메시지 큐가 통신을 이용한 설비라면, **공유 메모리는 데이터 자체를 공유하도록 지원하는 설비**다.
    
    프로세스의 메모리 영역은 독립적으로 가지며 다른 프로세스가 접근하지 못하도록 반드시 보호되야한다. 하지만 다른 프로세스가 데이터를 사용하도록 해야하는 상황도 필요할 것이다. 파이프를 이용해 통신을 통해 데이터 전달도 가능하지만, **스레드처럼 메모리를 공유**하도록 해준다면 더욱 편할 것이다.
    
    공유 메모리는 **프로세스간 메모리 영역을 공유해서 사용할 수 있도록 허용**해준다.
    
    프로세스가 공유 메모리 할당을 커널에 요청하면, 커널은 해당 프로세스에 메모리 공간을 할당해주고 이후 모든 프로세스는 해당 메모리 영역에 접근할 수 있게 된다.
    
    - **중개자 없이 곧바로 메모리에 접근할 수 있어서 IPC 중에 가장 빠르게 작동함**
    
5. **메모리 맵**
    
    공유 메모리처럼 메모리를 공유해준다. 메모리 맵은 **열린 파일을 메모리에 맵핑시켜서 공유**하는 방식이다. (즉 공유 매개체가 파일+메모리)
    
    주로 파일로 **대용량 데이터를 공유**해야 할 때 사용한다.
    
    (파일의 내용을 메모리에 반영하고, 이를 통해 프로세스 간에 데이터를 공유합니다. 파일을 읽거나 쓰는 것처럼 메모리에 접근)
    
6. **소켓**
    
    **네트워크 소켓 통신을 통해 데이터를 공유**한다.
    
    클라이언트와 서버가 소켓을 통해서 통신하는 구조로, 원격에서 프로세스 간 데이터를 공유할 때 사용한다.
    
    서버(bind, listen, accept), 클라이언트(connect)
    

이러한 IPC 통신에서 프로세스 간 데이터를 동기화하고 보호하기 위해 세마포어와 뮤텍스를 사용한다. (공유된 자원에 한번에 하나의 프로세스만 접근시킬 때)

- +
    
    IPC는 동시에 실행되는 여러 프로세스 간에 **정보를 전송하고 동기화하기 위해 사용**됩니다. **세마포어와 뮤텍스**는 IPC에서 발생할 수 있는 문제 중 하나인 **경쟁 조건 및 동시 접근 문제**를 해결하는 데 사용
    
    1. **경쟁 조건 (Race Condition):** 여러 프로세스가 공유 자원에 동시에 접근하고 수정할 때 발생할 수 있는 문제. 예를 들어, 두 프로세스가 **동시**에 같은 변수를 변경하려고 할 때 문제가 발생할 수 있습니다.
    2. **동시 접근 문제 (Concurrency Issues):** 여러 프로세스가 **동시에 실행**되는 경우, 공유 자원에 동시에 접근하는 것이 예상치 못한 결과를 초래할 수 있습니다.
    
    - **세마포어**
        - 리소스에 동시 허용이 가능한 스레드의 수를 제어하는 데 사용됨
        - 소유 권한이 없으므로, 잠금을 획득하지 않은 쓰레드도 signal 연산을 사용하여 잠금을 해제할 수 있음
        - 초기 값을 설정할 수 있으며, 이 값은 허용 가능한 동시 액세스 수를 나타냄
        - **wait (P)와 signal (V) 연산을 통해 제어됨**
    - **뮤텍스**
        - 임계 영역을 보호하여 데이터 무결성을 보장하기 위해 사용됨
        - 소유 권한을 가지므로, 잠금을 획득한쓰레드만 잠금을 해제할 수 있음
        - 주로 이진 세마포어(Binary Semaphore)로 초기화되며, 두 가지 상태(잠금 상태와 잠금 해제 상태)만 가짐
        - **lock과 unlock 연산을 통해 제어됨**
    
    세마포어와 뮤텍스는 다수의 프로세스 간의 동기화와 상호 배제를 가능케 하여 공유 자원에 안전한 접근을 보장합니다. 이들을 올바르게 사용함으로써 경쟁 조건 및 데이터 일관성 문제를 효과적으로 해결할 수 있습니다.
    

### 예상질문

### **프로세스의 특징을 설명하세요.**

- 프로세스는 각각 독립된 메모리 영역(Code, Data, Stack, Heap의 구조)을 할당받는다.
- 기본적으로 프로세스당 최소 1개의 스레드(메인 스레드)를 가지고 있다.
- 각 프로세스는 별도의 주소 공간에서 실행되며, 한 프로세스는 다른 프로세스의 변수나 자료구조에 접근할 수 없다.
- 한 프로세스가 다른 프로세스의 자원에 접근하려면 프로세스 간의 통신(IPC, inter-process communication)을 사용해야 한다. (Ex. 파이프, 파일, 소켓 등을 이용한 통신 방법 이용)

### 소켓이란 무엇입니까?

- 소켓은 두 응용 프로그램을 연결하는 데 사용된다. 연결의 끝점을 소켓이라고 한다.

### 커널이란 무엇입니까?

- 커널은 OS의 모든 부분에 대한 기본 서비스를 제공하는 컴퓨터 운영 체제의 핵심이자 가장 중요한 부분이다.
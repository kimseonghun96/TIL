# 이임충

## ****PCB & Context Switching****

### Process Management

할 일이 여러 개일 때, 노션, 다이어리 등으로 일정 관리

프로세스가 여러 개일 때, CPU 스케쥴링을 통해 관리하는 것을 말함

- CPU 스케쥴링
  
    Ready 상태의 프로세스 중에서 어떤 프로세스에게 CPU를 할당할지 결정

관리할 때, 각 프로세스들이 뭔지 알아야 관리 

노션에다가 제목이나 담당한 인원, 날짜 등을 적는 것처럼

각 프로세스들이 뭔지 == 프로세스 정보 == Process Metadata

**Process Metadata**

- Process ID
  
    프로세스 식별자

- Process State
  
  - 생성(create), 준비(ready), 실행 (running), 대기(waiting), 완료(terminated) 상태
    
      ![Untitled](%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%B5%E1%86%B7%E1%84%8E%E1%85%AE%E1%86%BC%20f189bc5e660b4434a9d76be71ce47a3a/Untitled.png)
    
    - 생성(create) 상태
      
        프로그램이 메모리에 올라가 프로세스가 되고
      
        운영체제에 의해 프로세스 제어 블럭(PCB)가 생성
    
    - 준비(ready) 상태
      
        프로세스가 생성되면 바로 CPU에 할당되어 실행되는 것이 아니라 준비 상태
      
        PCB는 준비 큐에 들어가며 CPU에 할당될 때까지 자신의 차례를 기다림
      
        어떤 프로세스가 실행 상태로 옮겨지는가는 CPU 스케줄러에 의해 관리
    
    - 실행 (running) 상태
      
        CPU 스케줄러에 의해 프로세스가 실행 상태가 되면 CPU를 할당받아 작업을 진행
      
        시분할 시스템의 경우에는 타임 슬라이스가 주어지기 때문에 이 시간동안만 프로세스가 CPU를 사용
      
        주어진 타임 슬라이스동안 작업을 완료하지 못하면 타임아웃(timeout) 즉, 인터럽트가 발생하며 실행 상태의 프로세스는 작업을 중단하고 다시 준비 상태가 된다
    
    - 대기(waiting) 상태
      
        만약 실행 중인 프로세스가 입출력을 요청하는 경우에는 CPU 작업을 중단하고 입출력을 처리
      
        → CPU는 입출력 관리자에게 입출력 요청
      
        → block 명령이 발생하며 프로세스는 입출력이 끝날 때까지 대기 상태
    
    - 완료(terminated) 상태
      
        프로세스가 작업을 모두 완료하면 종료
      
        메모리에 적재되었던 프로세스 정보와 프로세스 제어 블럭(PCB)가 제거

- Process Priority
  
    우선순위, 사용자가 지정 X
  
    우선순위가 높으면 Realtime Process, 우선순위가 낮으면 Normal Process

- CPU Register

- Owner

- CPU Usage

- Memory Usage

### Process Control Block

프로세스 메타데이터들을 저장해 놓는 곳, 한 PCB 안에는 한 프로세스의 정보가 담김

![process 내부 공간](%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%B5%E1%86%B7%E1%84%8E%E1%85%AE%E1%86%BC%20f189bc5e660b4434a9d76be71ce47a3a/Untitled%201.png)

process 내부 공간

**정리**

프로그램 실행 → 프로세스 생성 → 프로세스 주소 공간에 (코드, 데이터, 스택) 생성
→ 이 프로세스의 메타데이터들이 PCB에 저장

**추가 자료**

[PCB(Process Control Block)란?](https://jwprogramming.tistory.com/16)

### PCB가 필요한 이유

CPU에서는 프로세스의 상태에 따라 교체작업이 발생

예를 들어, interrupt가 발생해서 할당받은 프로세스가 waiting 상태가 되고 다른 프로세스를 running으로 변경할 때

이때, 앞으로 다시 수행할 대기 중인 프로세스에 관한 저장 값을 PCB에 저장해두는 것이다.

### PCB 관리 방식

Linked List 방식

PCB List Head에 PCB들이 생성될 때마다 붙음

주소값으로 연결된 연결리스트 방식이므로 삽입 삭제가 용이

프로세스가 완료되면 제거됨

Queue에 PCB가 저장됨 

[[운영체제] 프로세스 큐, Swap](https://velog.io/@profile_exe/운영체제-Queue-Swap)

### Context Switching

수행 중인 프로세스 변경할 때, CPU 레지스터 정보가 변경되는 것

CPU가 이전의 프로세스 상태를 PCB에 보관하고, 

또 다른 프로세스의 정보를 PCB에 읽어 레지스터에 적재하는 과정

**상황**

인터럽트가 발생

실행 중인 CPU 사용 허가시간을 모두 소모

입출력을 위해 대기

= Ready → Running, Running → Ready, Running → Waiting처럼 상태 변경

**Context Switching의 Overhead**

Overhead는 과부하 → 보통 안좋은 말

프로세스 작업 중에는 ****OverHead를 감수

프로세스를 수행하다가 입출력 이벤트가 발생해서 대기 상태로 전환시킴
이때, CPU를 그냥 놀게 놔두는 것보다 다른 프로세스를 수행시키는 것이 효율적

→ 노는 꼴을 못본다

계속 프로세스를 수행 → 다른 프로세스를 실행시키고 Context Switching 하는 것

다른 프로세스를 실행시키고 Context Switching 하는 것

- 좀 더 - context switching
  
    하나의 일만 처리할 수 있다면, 한 가지 일을 하는 동안 다른 일을 못함
  
    → 하나의 일을 할 때, 다른 일은 대기
  
    → 속도가 느림
  
    빠른 속도로 일을 바꿔가면서 실행 
  
    → 실시간으로 처리하는 것처럼 보임
  
    → Context Switching이 필요
  
    **비용 문제**
  
  - 캐시 초기화
  
  - 메모리 매핑 초기화
    
      메모리 맵
    
      [운영 체제](https://ko.wikipedia.org/wiki/%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C)에서 [파일](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC)을 다루는 방법
    
      메모리 맵 파일을 통해 [프로세스](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)의 [가상 메모리](https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A9%94%EB%AA%A8%EB%A6%AC) 주소 공간에 파일을 매핑한 뒤 
    
      [가상 메모리](https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A9%94%EB%AA%A8%EB%A6%AC) 주소에 직접 접근하는 것으로 파일 읽기/쓰기를 대신
  
  - 커널은 항상 실행 - 메모리 접근을 위해서

- 출처
  
  1. CPU 스케쥴링
     
      [[운영체제(OS)] CPU 스케줄링 - (1) CPU 스케줄링의 개념 (tistory.com)](https://kjhoon0330.tistory.com/entry/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9COS-CPU-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81#2.%201.%E2%8F%B0CPU%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81%EC%9D%B4%EB%9E%80)
  
  2. 프로세스 상태
     
      [[OS] 프로세스 상태](https://lotuslee.tistory.com/85)
  
  3. Process Priority
     
      [Ubuntu Process의 Priority와 Niceness 설정하기](https://newsight.tistory.com/349)
  
  4. Context Switching 추가 설명
     
      [Context Switching이란?](https://nesoy.github.io/articles/2018-11/Context-Switching)
  
  5. 메모리 맵
     
      [메모리 맵 파일](https://ko.wikipedia.org/wiki/메모리_맵_파일)
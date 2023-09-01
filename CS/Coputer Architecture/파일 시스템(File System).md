## 파일 시스템****(File System)****

> 컴퓨터에서 파일이나 자료를 쉽게 발견할 수 있도록, 유지 및 관리하는 방법이다. 저장 매체에는 수많은 파일이 있기 때문에, 이런 파일들을 관리하는 방법을 말한다.

→ 파일과 디렉터리를 보조기억장치에 할당하고 접근하는 방법

### 파티셔닝과 포매팅

- 이제 막 공장에서 생산되어 한 번도 사용된 적 없는 새 하드 디스크 or SSD?
  
  → 곧 바로 파일을 생성하거나 저장할 수는 없다.
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/8325d012-7726-44b0-9dab-1bc12f77a025/Untitled.png)

- 그래서 파티셔닝과 포매팅을 해야한다.
1. **파티셔닝**
   
   - 저장 장치의 논리적인 영역을 구획하는 작업

2. **포매팅**
   
   - 파일 시스템을 설정
   - 어떤 방식으로 파일을 관리할지 결정, 새로운 데이터를 쓸 준비하는 작업

→ 파티셔닝과 포매팅을 완료하여 파일 시스템을 설정했다면 **파일과 디렉터리 생성이 가능**

**파일 시스템의 특징**

- 커널 영역에서 동작
- 파일 CRUD 기능을 원활히 수행하기 위한 목적
- 게층적 디렉터리 구조를 가짐
- 디스크 파티션 별로 하나씩 둘 수 있음

**개발목적**

- 하드디스크와 메인 메모리 속도차를 줄이기 위함
- 파일 관리
- 하드디스크 용량 효율적 이용

**구조**

- 메타 영역 : 데이터 영역에 기록된 파일의 이름, 위치, 크기, 시간정보, 삭제유무 등의 파일 정보
- 데이터 영역 : 파일의 데이터

### 파일 구조

1. **순차 파일 구조(Sequential File Structure)**

- 일반 파일은 기본적으로 순차 파일 구조이다. 순차 파일 구조는 파일 내용이 하나의 긴 줄로 늘어선 형태로 카세트 테이프가 대표적인 예이다.

- **장점**
  
  1. 모든 데이터가 순서대로 기록되기 때문에 저장 공간에 낭비되는 부분이 없다.
  
  2. 구조가 단순하다.
  
  3. 순서대로 데이터를 읽거나 저장할 때 매우 빠르게 처리된다.

- **단점**
  
  1. 파일에 새로운 데이터를 삽입하거나 삭제할 때 시간이 많이 걸린다.
  
  2. 특정 데이터로 이동할 때 직접 접근이 어렵기 때문에 앞에서부터 순서대로 움직여야 한다.

2. **인덱스 파일 구조(Index File Structure)**

- **순차 파일 구조에 `인덱스 테이블`을 추가하여 순차 접근과 직접 접근이 가능하다.**

- **현대의 파일 시스템은 인덱스 파일 구조**로,
  
  **파일을 저장할 때는 순차 파일 구조로 저장**하고, **파일에 접근할 때는 인덱스 테이블을 보고 원하는 파일에 접근**한다.

- `데이터베이스`와 같이 데이터의 빠른 접근이 필요한 시스템에 사용된다.

3. **직접 파일 구조(Direct File Structure)**

- 저장하려는 데이터의 특정 값에 어떤 관계를 정의하여 물리적인 주소로 변환하는 파일 구조이다.
- **특정 함수를 이용하여 직접 접근이 가능한 파일 구조이며, 이때 사용하는 함수를 `해시 함수`라고 한다.**
- 해시 함수를 이용하여 주소를 변환하기 때문에 데이터 접근이 매우 빠르지만, 해시 함수를 선정하는 것이 큰 중요 포인트이다.

### 파일 할당 방법

- 포매팅까지 끝난 하드 디스크에 파일을 저장하기
- 운영체제는 파일/디렉터리를 블록 단위로 읽고 쓴다.
  - 즉, 하나의 파일이 보조기억장치에 저장될 대에는 여러 블록에 걸쳐 저장된다.
  - (하드 디스크의 가장 작은 저장 단위는 섹터, 하지만 보통 블록 단위로 읽고 사용)
- 파일을 보조 기억장치에 할당하는 두 가지 방법 : 연속 할당, 불연속 할당

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/610811ae-a5ae-4f09-8145-7e8e0801042c/Untitled.png)

1. 연속 할당
   
   - 이름 그대로 보조기억장치 내 연속적인 블록에 파일 할당
   - 연속된 파일에 접근하기 위해 파일의 첫 번째 블록 주소와 블록 단위의 길이만 알면 된다.
   - 디렉터리 엔트리 : 파일 이름 & **첫 번째 블록 주소 & 블록 단위 길이 명시**
   
   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/6cbe857f-d5c9-4561-9f48-9da0d9dde46c/Untitled.png)
   
   - 단점 : 구현이 단순하지만 외부 단편화를 가져 올 수 있다.
     
     (중간에 삭제 됐을 때, 잔여 블록은 11개지만 블록 7개 이상 사용하는 파일은 할당x)
   
   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/f60980dc-9217-4bad-a5cb-6b19e41a8860/Untitled.png)

2. **불연속 할당** (오늘날 주로 쓰이는 할당)
   
   - 연결 할당
     
     - 각 블록의 일부에 다음 블록의 주소를 저장하여 각 블록이 다음 블록을 가리키는 형태로 할당
     - 파일을 이루는 데이터 블록은 연결 리스트로 관리
     - 불연속 할당의 일종 : 파일이 여러 블록에 흩어져 저장되어도 무방
     
     ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/041d2fb6-8c14-4864-bac3-942dfdc8e802/Untitled.png)
     
     - 디렉터리 엔트리 : 파일 이름 & 첫번째 블록 주소 & 블록 단위의 길이
     
     ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/a503f72c-7956-4dec-8486-5864d28c8dc2/Untitled.png)
     
     → 끝났을 때 끝났음을 알려주는 것을 명시해야됨 위 그림에서는 -1
     
     - 단점:
       - 반드시 첫 번째 블록부터 하나씩 읽어들여야 한다. - 임의 접근 속도가 느림
       - 오류 발생 시 해당 블록 이후 블록은 접근이 어렵다.
   
   - 색인 할당
     
     - 파일의 모든 블록 주소를 색인 블록이라는 하나의 블록에 모아 관리하는 방식
     - 파일 내 임의의 위치에 접근하기 용이
     
     ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/abb5200f-cadb-47d3-88e8-5b8cdca976b4/Untitled.png)
     
     - 디렉터리 엔트리 : 파일 이름 & 색인 블록 주소

### 파일 시스템 살펴보기

- **FAT 파일 시스템 (윈도우)**
  
  - 연결 할당 기반 파일 시스템
  - 연결 할당의 단점을 보완 - FAT가 메모리에 캐시될 경우 임의 접근 속도 개선 가능
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/75db91b7-4436-4884-a2a5-1cfa93cc3759/Untitled.png)
  
  - 각 블록에 포함된 다음 블록 주소를 한데 모아 테이블(FAT ; File Allocation Table)로 관리
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/7d9eb710-33ce-46b3-8221-ef708bf7f7c2/Untitled.png)
  
  - 디렉터리 엔트리 (파일의 속성까지 기록)
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/7445b95a-de9e-4c8f-9345-657af7e01caa/Untitled.png)
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/4a1860d4-fd34-424e-ae6c-4b3f500f5856/Untitled.png)
  
  1. 가장 먼저 루트 디렉터리에 접근
  2. home이 3번에 있음 → minchul 15 → [a.sh](http://a.sh) 9번
  3. 9, 8, 11, 13번 블록에 접근하게된다.

- **유닉스 파일 시스템 (유닉스)**
  
  - 색인(index) 할당 기반 파일 시스템
  
  - 색인 블록 == i-node
    
    - 파일의 속성 정보와 15개의 블록 주소 저장 가능
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/0a54ca6e-ec2d-46af-94f7-fc648ba82792/Untitled.png)
    
    → i-node마다 고유한 번호가 있고, 이것만 보더라도 모든 걸 알 수 있다.
  
  - 파티션 : i-node 한 곳에 모여있음
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/e844fa1b-4440-4e0f-ad6e-2d562092719b/Untitled.png)

- 15개 이상의 큰 블록인 경우에는?
  
  1. 블록 주소 중 12개에는 직접 블록 주소 저장
     
     1. 직접 블록 : 파일 데이터가 저장된 블록
     
     ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/7d533e02-6b26-4760-b8c2-0d0ab061c713/Untitled.png)
  
  2. 1번으로 충분하지 않다면 13번째 주소에 단일 간접 블록 주소 저장
     
     1. 단일 간접 블록 : 파일 데이터를 저장한 블록 주소가 저장된 블록
     
     ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/9b64487a-d451-48bd-883f-e2a958167c72/Untitled.png)
  
  3. 2번으로 충분하지 않다면 14번째 주소에 이중 간접 블록 주소 저장
     
     1. 이중 간접 블록 : 단일 간접 블록들의 주소를 저장하는 블록
     
     ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/beccc22d-ea67-4529-9f9d-8f4191a5d7da/Untitled.png)
  
  4. 3번으로 충분하지 않다면 15번째 주소에 삼중 간접 블록 주소 저장
     
     1. 삼중 간접 블록 : 이중 간접 블록들의 주소를 저장하는 블록
     
     ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/be3ac949-6ea7-43ea-b92b-9c1096761dd8/Untitled.png)

- 디렉터리 엔트리 : i - node가 파일 시스템의 핵심

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/580cf6e3-4060-494f-abde-e00e864536e8/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/5156bf59-fa81-4702-b972-10153d7c53d8/Untitled.png)

1. 루트 디렉터리에 접근 - 2번 node에 접근 해서 1번을 봄
2. home이 i-node 3번 → 210블록
3. minchul i-node 8번 → 121블록
4. [a.sh](http://a.sh) i-node 9 → 98, 12, 13 블록

참조 [[컴퓨터 공학 기초 강의] 42강. 파일 시스템(완강) - YouTube](https://www.youtube.com/watch?v=C-IYRzC-GW8)

### 해시(Hash)

### 기본

1. **해시(Hash) : 값**
   
   단방향 암호화 기법인 해시함수(HashFunction)을 이용하여 생성된 고정된 길이의 비트열
   
   (출처: [](https://velog.io/@kwj2435/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Hash-HashMap-HashTable)[https://velog.io/@kwj2435/자료구조-Hash-HashMap-HashTable](https://velog.io/@kwj2435/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Hash-HashMap-HashTable))

2. **해시 함수(Hash Function) : 함수**
   
   데이터의 효율적 관리를 목적으로
   
   임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수
   
   (출처: [](https://ratsgo.github.io/data%20structure&algorithm/2017/10/25/hash/)https://ratsgo.github.io/data structure&algorithm/2017/10/25/hash/)

3. **해시 테이블(HashTable 혹은 해시 맵 HashMap): 자료구조**
   
   해시함수를 사용하여 키를 해시값으로 매핑하고,
   
   이 해시값을 색인(Index) 혹은 주소 삼아 데이터의 값(value)을 키와 함께 저장하는 자료구조
   
   ![해시 테이블 예시 + 충돌 예시](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/0148327f-f2ee-4fbb-b71d-819a9a4a5dcd/%ED%95%B4%EC%8B%9C_%ED%85%8C%EC%9D%B4%EB%B8%94_%EC%98%88%EC%8B%9C.png)
   
   해시 테이블 예시 + 충돌 예시
   
   - 데이터가 저장되는 곳 == 버킷(bucket) 또는 슬롯(slot)
     
     ![해시 테이블 예시 02.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/6a4704ad-ec96-4991-a695-ee509c86647e/%ED%95%B4%EC%8B%9C_%ED%85%8C%EC%9D%B4%EB%B8%94_%EC%98%88%EC%8B%9C_02.png)

**대략적인 구조**

해시_값 = 해쉬_함수(키)

**키(key):** 매핑 전 원래 데이터의 값

**해시값(hash value):** 매핑 후 데이터의 값

**해싱(hashing):** 매핑하는 과정 자체

**장점**

1. 적은 자원으로 많은 데이터를 효율적으로 관리
   
   클라우드나 하드 디스크에 존재하는 무한한 데이터 → 유한한 개수의 해시값으로 매핑
   
   작은 메모리로도 프로세스 관리가 가능

2. 색인(index)에 해시값을 사용함 + 언제나 동일한 해시값 리턴
   
   모든 데이터를 살피지 않아도 검색과 삽입/삭제를 빠르게 수행
   
   해당 색인만 알면 해시테이블의 크기에 상관없이 데이터에 대단히 빠르게 접근

3. 색인은 계산이 간단한 함수(**상수시간 O(1)**)로 작동
   
   이진탐색트리 - 메모리를 효율적으로 사용, 데이터 탐색에 소요되는 계산복잡성은 O(logn)
   
   배열 - 데이터 탐색에 따른 계산복잡성은 O(1), 메모리를 미리 할당

**문제점**

**collision 현상**

대부분 해쉬 값(해시 함수를 통해 나온 결과 값)보다 키 값(== 실제 데이터 값)이 많음

- 추가 - 해쉬 값과 키의 차이에 대한 내용
  
  Direct-address table: 키의 전체 개수 == 버킷의 크기을 가진 해시테이블
  
  키 갯수(n) > 해시 테이블의 크기(m)인 해시 테이블을 더 많이 운용
  
  **load factor**(α) == n/m
  
  해시테이블의 한 버킷에 평균 몇 개의 키가 매핑되는가를 나타내는 지표
  
  Direct-address table의 load factor는 1 이하이며, 1보다 큰 경우 해시충돌 문제
  
  - Direct-address table의 load factor는 1 이하가 되는 경우
    
    ![해시 테이블 예시 03.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/71a56237-2094-4cf2-9008-abb8dbdd3be5/%ED%95%B4%EC%8B%9C_%ED%85%8C%EC%9D%B4%EB%B8%94_%EC%98%88%EC%8B%9C_03.png)

데이터가 많아지면, 다른 데이터가 같은 해시 값으로 충돌나는 현상이 발생함

거의 모든 해시함수는 해시충돌을 일으키는 것

충돌을 줄이는 것도 의미가 있지만,

중요한 것은 해시 충돌이 해시값 전체에 걸쳐 균등하게 발생하게끔 하는 것

전체에 걸쳐야 하는 이유:

모든 키가 한 값으로만 매핑이 된다면

데이터를 액세스할 때 비효율성

보안이 취약 → 서로 다른 키인데도 동일한 해시값

**충돌 문제 해결 - 빠진 내용: 각 해결법에 대한 삽입, 삭제, 탐색 연산에 대한 설명**

1. **체이닝**
   
   연결리스트로 노드를 계속 추가해나가는 방식
   
   (제한 없이 계속 연결 가능, but 메모리 문제)
   
   한 버킷당 들어갈 수 있는 엔트리의 수에 제한을 두지 않음
   
   ![해시 테이블 예시 04.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/d543f426-1fdb-440b-8695-967982378e76/%ED%95%B4%EC%8B%9C_%ED%85%8C%EC%9D%B4%EB%B8%94_%EC%98%88%EC%8B%9C_04.png)
   
   최근 데이터는 연결리스트의 *head*에 추가하면 시간 복잡도: O(1)
   
   연결리스트의 tail에 추가할 경우 O(n)이 됨
   
   → 아마 연결리스트를 하나씩 탐색해서 맨 마지막에 붙기 때문이 아닌가?

2. **Open Addressing**
   
   해시 함수로 얻은 주소가 아닌 다른 주소에 데이터를 저장할 수 있도록 허용
   
   (해당 키 값에 저장되어있으면 다음 주소에 저장)
   
   한 버킷당 들어갈 수 있는 엔트리가 하나뿐
   
   메모리 문제가 발생하지 않으나 해시충돌이 발생할 수 있음
   
   ![해시 함수: 주어진 수를 7로 나누는 예시](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/a9414900-7a31-4baf-9cf3-47e86a8cfe34/%EC%98%A4%ED%94%88_%EC%96%B4%EB%93%9C%EB%A0%88%EC%8B%B1_%EC%98%88%EC%8B%9C.png)
   
   해시 함수: 주어진 수를 7로 나누는 예시
   
   - 탐사 - Probing
     
     1. **선형 탐사**
        
        정해진 고정 폭으로 옮겨 해시값의 중복을 피함
        
        - 추가 - 선형 탐사
        
        해시값에 해당하는 버킷에 다른 데이터가 저장돼 있으면
        
        해당 해시값에서 고정 폭(예컨대 1칸)을 옮겨 다음 해시값에 해당하는 버킷에 액세스(삽입, 삭제, 탐색)
        
        특정 해시값 주변 버킷이 모두 채워져 있는 primary clustring 문제에 취약
        
        ![선형 탐사 단저.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/0697a337-5dce-455a-b85d-c7c4d112e0ec/%EC%84%A0%ED%98%95_%ED%83%90%EC%82%AC_%EB%8B%A8%EC%A0%80.png)
     
     2. **제곱 탐사**
        
        정해진 고정 폭을 제곱수로 옮겨 해시값의 중복을 피함
        
        - 추가 - 제곱 탐사 설명
        
        여러 개의 서로 다른 키들이 동일한 초기 해시값(아래에서 *initial probe*)을 갖는 secondary clustering에 취약
        
        ![제곱 탐사 단점.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/44f8075c-fef9-4f93-a959-f4f2c5eaccf5/%EC%A0%9C%EA%B3%B1_%ED%83%90%EC%82%AC_%EB%8B%A8%EC%A0%90.png)

      open addressing은 해시테이블에 데이터가 꽉 차지 않는다는 걸 전제
    
      키들을 모든 버킷에 균등하게 할당한다고 가정

---

### 추가

**사용처**

1. 보안 분야
   
   직접적인 연관이 없기 때문에 해시 값만 가지고는 키를 온전히 복원하기 어렵

2. 데이터 축약 기능
   
   서로 다른 입력데이터에 대해 일정한 길이의 출력

3. 파일 위/변조 확인

**해시 테이블의 기본 연산**

삽입, 삭제, 탐색(search)

**충돌 문제 해결**

1. 이중해싱(double hashing)
   
   탐사할 해시값의 규칙성을 없애버려서 clustering(데이터들이 뭉치는 것)을 방지
   
   2개의 해시함수를 준비
   
   하나는 최초의 해시값을 얻을 때,
   
   또 다른 하나는 해시충돌이 일어났을 때 탐사 이동폭을 얻기 위해 사용

2. **해시함수로 해시충돌을 완화하는 방법**
   
   특정 값에 치우치지 않고 해시값을 고르게 만들어내는 해시함수가 좋은 해시함수
   
   1. ****division method****
      
      숫자로 된 키를 해시테이블 크기으로 나눈 나머지를 해시값
      
      해쉬 값 = 숫자로 된 키 값 % 해시 테이블 크기;
      
      키 값 = 숫자로 된 키
      
      해시 함수 = % 해시 테이블 크기
      
      해시 테이블 크기
      
      대개 소수(prime number)를 사용
      
      특히 2의 제곱수와 거리가 먼 소수를 사용하는 것이 좋다
      
      장점: 간단하면서도 빠른 연산
      
      단점: 해시함수 특성 때문에 해시테이블 크기가 정해진다
   
   2. ****multiplication method****
      
      해쉬 테이블 크기보다 큰 수를 해쉬 테이블 크기 범위에 들어오도록 수축
      
      해쉬 함수 = ((숫자로 된 키 값 * 실수(0 ~ 1)) % 1) * 테이블 크기
      
      % 1을 하는 이유는 소수부만 취하기 위해서
      
      테이블 크기는 얼마가 되든 크게 중요하지는 않으며 보통 2의 제곱수
      
      장점?: 2진수 연산에 최적화한 컴퓨터 구조를 고려한 해시함수
      
      단점: 나눗셈법보다는 다소 느린 편
   
   3. ****universal hasing****
      
      다수의 해시함수를 만들고 무작위로 해시함수를 선택해 해시값을 만드는 기법
      
      목적: 임의의 키값을 임의의 해시값에 매핑할 확률을 1/m로 만드려는 것이 목적
      
      m은 해시 테이블 크기
      
      특정 조건의 해시함수 집합은 1/m로 만드는 게 가능

---

### 면접에서 물어볼 만한 질문

---

- **굳이?**
  
  1. 유명한 해시 알고리즘
     
     Message-Digest Algorithm(MD) - MD5
     
     Secure Hash Algorithm([SHA](https://namu.wiki/w/SHA))-N
  
  2. C++
     
     C++에서는 STL에서 hash_map, hash_set이 존재
     
     map과 set 컨테이너는 자료를 정렬하여 저장
     
     map, set의 사용하는 경우 : 정렬된 상태로 자료 저장을 하고 싶을 때
     
     hash_map, hash_set은 정렬 하지 않으며 자료를 저장
     
     hash_map, hash_set : 정렬이 필요 없으며 빠른 검색을 원할 때.
  
  3. Python
     
     hash를 사용하기 위한 라이브러리들이 내장
     
     from hashlib import md5
     
     hash_value = md5(값.encode('utf8')).hexdigest()
  
  4. Javascript
     
     1. URL.hash
        
        URL 인터페이스의 hash 속성
        
        ![출처: URL.hash - Web API | MDN (mozilla.org)](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/8af49407-03ae-4999-89ae-77bb3c683e85/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8_%ED%95%B4%EC%8B%9C_%ED%95%A8%EC%88%98.png)
        
        출처: [URL.hash - Web API | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/API/URL/hash)
     
     2. hash 설명
        
        It is commonly in the form of a 128-bit "fingerprint" or "message digest".
        
        message digest
        메시지를 해시(Hash)하는 것을 의미한다.
        임의의 길이를 가진 메시지를 MD함수에 넣으면 일정한 길이를 가진 데이터를 얻는다.
        이 데이터를 비교해 위/변조 되었는지 쉽게 알 수 있다.
        
        finger print
        
        말 그대로 지문 - 솔라리스에 설치된 파일이 변조되었는지 MD5해시값을 통해 확인
        
        솔라리스 - 기업용 OS
  
  5. Java
     
     - 자바 객체에서의 해시
       
       저장_위치 = 해시_함수(키_값)
       
       객체의 특정 정보(키_값)을 매개변수 값으로 넣으면
       
       그 객체가 저장되어야 할 위치나 저장된 해시 테이블 주소(저장_위치)를 반환
       
       == 객체 정보(키_값)를 알면 해당 객체의 위치를 빠르게 검색할 수 있음
       
       → 해시 함수는 개발하는 프로그램 특성에 따라 다르게 구현
       
       (출처: DO IT! 자바 프로그래밍 입문. 11장 기본 클래스)
     
     - Object 클래스: 모든 자바 클래스의 최고 조상 클래스
       
       == 모든 자바 클래스는 Object에 있는 메서드를 사용 가능
       
       == 재정의
       
       - 재정의 예시
         
         Object의 메서드 중에 hashCode(): 해당 객체의 해시 코드값을 반환함.
         
         ![알고리즘 풀 때 생성한 CityMap이 Object 클래스의 hashCode() 함수를 재정의한 것](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/e3ca51ee-d0ef-4bf1-8bc8-6435ed68ae93/%EC%9E%90%EB%B0%94_%ED%95%B4%EC%8B%9C%EC%BD%94%EB%93%9C_%EC%9E%AC%EC%A0%95%EC%9D%98_02.png)
         
         알고리즘 풀 때 생성한 CityMap이 Object 클래스의 hashCode() 함수를 재정의한 것

      메서드 중에 toString(): 인스턴스(클래스로 생성된 객체)에 대한 정보
    
      == getClass().getName() + '@' + Integer.toHexString(hashCode())
    
      → 클래스_명@16진수_숫자값
    
      CityMap cityMap = new CityMap(사이즈);
    
      cityMap은 CityMap 클래스로 생성한 객체인 인스턴스
    
      cityMap은 인스턴스를 생성된 객체의 주소를 저장하는 참조변수
    
      cityMap(참조 변수)를 출력 → 16진수 숫자값
    
      == 해시코드 값
    
      == 자바 가상 머신이 힙 메모리에 저장한 '인스턴스의 주솟값’
    
      인스턴스가 같다면 hashCode() 메서드에서 반환하는 해시 코드 값이 같아야
    
      → hashCode()로 인스턴스 비교
    
    - 자바에서 HashTable과 HashMap의 차이
    
      가장 큰 차이는 Thread-safe
    
      HashTable은 Thread-safe함
    
      HashTable에서는 모든 Data 변경 메소드는 syncronized로 선언
    
      메소드 호출 전 스레드간 동기화 락을 통해 멀티 쓰레드 환경에서 data의 무결성을 보장
    
      HashMap은 Thread-safe하지 않기 때문에
    
      멀티 스레드 환경에서 동시에 객체의 data를 조작하는 경우 data가 깨질 수 있다
    
      - 스레드
    
        출처: https://velog.io/@gparkkii/ProgramProcessThread
    
        1. 프로그램
    
          컴퓨터에서 어떤 작업을 위해 실행할 수 있는 '정적인 상태'의 파일
    
          → 사용자가 원하는 일을 처리할 수 있도록 프로그래밍 언어를 사용하여 올바른 수행절차를 표현해 놓은 명령어들의 집합
    
          윈도우에서는 .exe파일
    
          ![exe 예시.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/8c52569b-8472-4ed1-b6cd-e0d189f77c26/exe_%EC%98%88%EC%8B%9C.png)
    
        2. 프로세스
    
          프로그램이 실행되서 돌아가고 있는 상태
    
          컴퓨터에서 연속적으로 실행되고 있는 '동적인 상태'의 컴퓨터 프로그램
    
          작업 관리자 창에서 표시되어 있는 동적인 상태의 프로그램
    
          ![프로세스.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/26a0e567-14d1-4531-824e-b26a2f729bbb/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4.png)
    
          프로그램을 실행 → 운영체제로부터 실행에 필요한 자원을 할당 → 프로세스
    
          프로세스는 최소 하나 이상의 스레드를 포함
    
        3. 스레드
    
          프로세스가 할당 받은 자원을 이용하는 실행 단위
    
          프로세스 내에서 프로세스의 자원을 이용해서 실제로 작업을 수행
    
          프로세스는 스레드의 컨테이너
    
          스레드가 소속된 프로세스가 운영체제로부터 자원을 할당받으면 그 자원을 스레드가 사용
    
        4. 멀티-스레드
    
          웹 서버는 대표적인 멀티 스레드 응용 프로그램
    
          스프링은 자바의 Thread 클래스를 직접 사용하지 않으며, 스레드 풀(스레드를 미리 여러 개 만들어 둔 것)을 사용하여 멀티 스레딩을 지원
    
          출처: [스프링의 싱글톤과 멀티 스레딩](https://80000coding.oopy.io/80fdeed4-c57b-440b-9f5b-edd62d2dd493)

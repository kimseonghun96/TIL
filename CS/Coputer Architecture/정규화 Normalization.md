## 정규화 Normalization

### 정의

데이터의 중복을 줄이고, 무결성을 향상시킬 수 있는 방법

- 무결성
  
  [컴퓨팅](https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%8C%85) 분야에서 완전한 [수명 주기](https://ko.wikipedia.org/w/index.php?title=%EC%A0%95%EB%B3%B4_%EC%88%98%EB%AA%85_%EC%A3%BC%EA%B8%B0_%EA%B4%80%EB%A6%AC&action=edit&redlink=1)를 거치며 [데이터](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0)의 정확성과 일관성을 유지하고 보증하는 것

**목표**

테이블 간 중복된 데이터를 허용하지 않는 것

무결성 유지 + DB 저장 용량을 효율적으로 관리

### 목적

1. 데이터의 중복을 없애면서 불필요한 데이터를 최소화시킨다.

2. 무결성을 지키고, 이상 현상을 방지한다.

3. 테이블 구성을 논리적이고 직관적으로 할 수 있다.

4. 데이터베이스 구조를 확장에 용이해진다.
- 이상현상
  
  **정의**
  
  데이터들이 불필요하게 중복되어 릴레이션 조작에 예기치 못한 문제
  
  - 릴레이션
    
    관계형 데이터베이스에서 정보를 구분하여 저장하는 기본 단위
    
    DB 테이블
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/2c9498d1-40c6-41d1-9c12-496532eaa385/Untitled.png)
  
  **종류**
  
  삽입할 때 잘못 삽입됨, 갱신할 때 잘못 갱신됨 등
1. 삽입 이상(Insertion Anomaly)
   
   데이터 삽입 시 의도와 다른 값들도 삽입됨

2. 삭제 이상(Delete Anomaly)
   
   데이터 삭제 시 의도와 다른 값들도 연쇄 삭제됨

3. 갱신 이상(Update Anomaly)
   
   속성값 갱신 시 일부 튜플만 갱신되어 모순 발생
- 튜플
  
  행
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/d184916d-0b55-4160-8874-9fc8b7c933f4/Untitled.png)
  
  **발생 이유**
  
  애트리뷰트들의 종속관계를 하나의 릴레이션에 표현하기 때문에 발생

- 애트리뷰트
  
  속성
  
  저장하고 싶은 개체의 항목들
  
  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/8f72420a-3756-4623-8720-700285c1991e/Untitled.png)

- 종속관계
  
  데이터베이스의 릴레이션(relation)에서 두 개의 속성(attribute) 집합 간 제약
  
  예를 들어 차량과 엔진 배기량을 추적 관리하는 시스템을 설계한다고 가정하겠습니다. 각 차량에는 차량별 고유한 차량 식별 번호(VIN)를 부여합니다. 그러면 "VIN → 배기량"이라고 적을 수 있습니다. 차량 한 대에는 배기량 하나만 있는 것이 맞기 때문입니다. (이 예제에서는 차량에 엔진이 하나만 달려 있다고 가정합니다.) 그러나 "배기량 → VIN"이라고 적는 것은 틀린 것입니다. 같은 배기량을 가진 여러 대의 차가 있을 수 있기 때문입니다.
  
  핸드폰 정보
  
  고유 시리얼 번호
  
  제품 명
  
  프로세서
  
  디스플레이 정보
  
  …
  
  고유 시리얼 번호 → 제품 명 (O)
  
  고유 시리얼 번호 → 메모리 (O)
  
  …
  
  디스플레이 정보 → 고유 시리얼 번호 (X)
  
  [[DataBase fundamentals] 데이터베이스 함수 종속성(Functional Dependency)에 대하여](https://firststep-de.tistory.com/6)
  
  [IT위키](https://itwiki.kr/w/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EC%A0%95%EA%B7%9C%ED%99%94#BCNF)
  
  [[Database] 데이터베이스 용어 - 릴레이션, 어트리뷰트, 튜플, 도메인, 차수, 카디널리티, 스키마](https://hoyeonkim795.github.io/posts/db-%EC%9A%A9%EC%96%B4/)

### 정규화 과정

각 정규화 과정은 이전 정규화 과정을 만족해야 한다.

1. 제 1 정규화 NF
   
   테이블 컬럼이 하나의 값(원자값)을 갖도록 테이블을 분리하는 과정
   
   **조건**
   
   1. 어떤 릴레이션에 속한 모든 도메인이 원자값만으로 되어 있어야한다.
   2. 모든 속성에 반복되는 그룹이 나타나지 않는다.
   3. 기본키를 사용하여 관련 데이터의 각 집합을 고유하게 식별할 수 있어야 한다.
   
   ![1000001803.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/8c7fbe5a-51f8-4612-a6e6-9fe47badb2d3/1000001803.jpg)

2. 제 2 정규화 2NF
   
   제 1 정규형을 만족
   
   테이블의 모든 컬럼이 완전 함수적 종속을 만족
   
   테이블에서 기본키가 복합키(키1, 키2)로 묶여있을 때, 두 키 중 하나의 키만으로 다른 컬럼을 결정지을 수 있으면 안된다
   
   ![1000001804.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/00a57ff4-76b4-418b-92f5-4c4877d32bf5/1000001804.jpg)

3. 제 3 정규화 3NF
   
   제 2 정규화가 진행된 상황
   
   이행적 종속을 없애기 위해 테이블을 분리
   
   A → B, B → C면 A → C가 성립된다
   
   **조건**
   
   기본키가 아닌 속성들은 기본키에 의존
   
   ![1000001801.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/37577ec2-3581-4ea6-8a05-199558c0806a/1000001801.jpg)

4. BCNF (Boyce and Codd Normal Form) - 사람 이름
   
   실질적인 정규화의 목표
   
   제 3 정규화를 만족하고 모든 결정자가 후보 키여야 한다는 것
   
   ![이 테이블에서 만큼은 강사 이름이 기본키로써 구분이 가능하다](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/a9393945-53da-4f8b-8788-e4a27f181072/1000001802.jpg)
   
   이 테이블에서 만큼은 강사 이름이 기본키로써 구분이 가능하다

5. 제 4 정규화 4NF
   
   다치 종속성을 제거
   
   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/a62ae1bb-2202-4109-8d9f-42251e327388/Untitled.png)
   
   101번 학생은 자바와 C++ 과목을 수강하고, 노래와 게임을 취미
   
   학생 번호 하나에 과목 여러 개와 취미 여러 개가 종속
   
   ![학생 번호를 토대로 값을 조회했을 때 나오는 중복](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/a0378b34-598c-4249-98ad-14a4434ce9af/Untitled.png)
   
   학생 번호를 토대로 값을 조회했을 때 나오는 중복
   
   과목과 취미는 관계가 없는 독립적인 관계지만
   
   같은 테이블의 학생 번호라는 칼럼에 다치 종속되어버려 중복이 발생
   
   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/5ba53ecf-f685-4ee1-b8af-12038777859c/Untitled.png)

6. 제 5 정규화 5NF
   
   중복을 제거하기 위해 분해할 수 있을 만큼 전부 분해
   
   조인 종속성 제거
   
   조인 연산을 했을 때 손실이 없어야
   
   잘 쓰이진 않음

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/7d03dfa4-5938-4f09-a037-fcd70412edf5/Untitled.png)

**조인 종속성**

A라는 릴레이션을 B와 C로 분해했다가 다시 조인했을 때 그대로 A가 되는 것

[IT위키](https://itwiki.kr/w/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EC%A0%95%EA%B7%9C%ED%99%94#4NF)

[[DB] 제 4정규형과 제 5정규형, 4NF와 5NF](https://code-lab1.tistory.com/270)

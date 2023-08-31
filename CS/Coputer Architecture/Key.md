# **Key**

---

> 조건에 만족하는 튜플을 찾거나 순서대로 정렬할 때 다른 튜플들과 구별할 수 있는 기준이 되는 속성

### 1**. Super Key (슈퍼키)**

> 각 행을 **유일하게 식별**할 수 있는 하나 또는 그 이상의 속성들의 집합 (유일성)

- 유일성 : Key로 하나의 Tuple을 유일하게 식별할 수 있음

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/4f6dce28-6931-4c17-bcd8-d98daf3501b5/Untitled.png)

### 2**. Candidate Key (후보키)**

> 테이블에서 **각 행을 유일하게 식별할 수 있는 최소한**의 속성들의 집합 ****(유일성 + 최소성)

- 최소성 : 꼭 필요한 속성으로만 구성

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/9d3f7a43-fd0f-444b-9e13-8bf3713b698c/Untitled.png)

### 3**. Primary Key (기본키)**

> 후보키들 중에서 하나를 선택한 키

- 테이블에서 오직 한개
- 최소성과 유일성을 만족
- NULL 값을 절대 가질 수 없고, 중복된 값을 가질 수 없음

### 4**. Alternate Key (대체키)**

> 후보키가 두개 이상일 경우 그 중에서 어느 하나를 기본키로 지정하고 남은 후보키

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/48ddfa50-0f49-47e6-8dba-32b37e2938a5/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/2e957cba-efb2-4d1b-9b6e-22a28b6ddd89/Untitled.png)

### **5. Foreign Key (외래키)**

> 다른 릴레이션의 기본키를 그대로 참조하는 속성의 집합

- 참조될(학생) 열의 값은 참조될(수강) 테이블에서 기본키(Primary Key)로 설정

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/3d8b2b65-719b-4b59-ae58-e1c60fedbb86/Untitled.png)

## SQL Injection

### 정의

해킹 방법 중 하나.

해커에 의해 조작된 SQL 쿼리문이 데이터베이스에 그대로 전달되어 비정상적 명령을 실행

### 공격 방법

해볼 수 있는 사이트

[SQL Injection - SQL Injection demo](https://www.codingame.com/playgrounds/154/sql-injection-demo/sql-injection)

1. 인증 우회
   
   1. 일반적인 상황
      
      일반적으로 로그인 시 아이디와 비밀번호를 입력
      
      예시
      
      아이디: admin 비밀번호: admin123
      
      ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/c2651edd-7ed2-4b31-9f2e-b4442053eafc/Untitled.png)
      
      ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/00721e1b-4506-4092-861f-ef07970054fa/Untitled.png)
      
      SQL 쿼리
      
      SELECT name FROM user WHERE username = ‘admin’ and password = ‘admin123’;
      
      쿼리 == 요청문
   
   2. 공격
      
      input 창에 비밀번호를 입력함과 동시에 다른 쿼리문을 함께 입력
      
      1. 다른 비밀번호를 입력했음에도 로그인 성공
      
      아이디: admin 비밀번호: 1234’ or ‘1’ = ‘1
      
      ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/f53bdd8c-de17-4739-90ce-d53b9751a294/Untitled.png)
      
      ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/2af9ce8e-ba18-4e4d-9ffc-1c5d6e2607c1/Untitled.png)
      
      SELECT name FROM user WHERE username = ‘admin’ and password = ‘1234’
      
      or ‘1’ = ‘1’;
      
      기본 쿼리문의 WHERE 절에 OR문을 추가하여 ‘1’ = ‘1’과 같은 true문을 작성
      
      무조건 적용되도록 수정한 뒤 DB를 마음대로 조작
      
      2. 동시에 삭제 명령문을 입력해도 로그인 성공
      
      ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/150de45a-07e3-45d4-afca-93b003dfda4e/Untitled.png)
      
      SELECT name FROM user WHERE username = ‘admin’ and password = ‘admin123’;
      
      DELETE * FROM user;
      
      비밀번호가 아이디와 일치해서 True가 되고
      
      뒤에 작성한 DELETE 문도 데이터베이스에 영향을 줄 수도 있게 되는 치명적인 상황

2. 데이터 노출
   
   시스템에서 발생하는 에러 메시지를 이용해 공격
   
   보통 에러는 개발자들이 버그 수정 용도로 사용
   
   해커들은 이를 역이용해 악의적인 구문을 삽입하여 에러를 유발
   
   예시
   
   GET 방식으로 동작하는 URL 쿼리 스트링을 추가하여 에러를 발생
   
   해당 웹앱의 데이터베이스 구조를 유추하여 해킹에 활용

### 방어 방법

1. 입력값을 받을 때, 특수문자 여부 검사
   
   로그인 전, 검증 로직을 추가하여 미리 설정한 특수문자들이 들어왔을 때 요청을 막아낸다

2. SQL 서버 오류 발생 시, 해당하는 에러 메세지 감추기
   
   view를 활용하여 원본 데이터베이스 테이블에는 접근 권한을 높인다
   
   일반 사용자는 view로만 접근하여 에러를 볼 수 없도록 만든다
   
   - 데이터베이스 view
     
     테이블로부터 유도된, 이름을 가지는 가상 테이블
     
     저장장치 내에 물리적으로 존재하지 않음
     
     장점
     
     필요한 데이터만 뷰로 정의해서 처리
     
     뷰를 통해서만 데이터에 접근하게 하면 뷰에 나타나지 않는 데이터를 안전하게 보호

3. preparestatement 사용하기
   
   - preparestatement / statement
     
     SQL문을 실행할 수 있는 객체
     
     가장 큰 차이점은 재사용 가능 여부
     
     statement
     
     예시
     
     String sqlstr = "SELECT name, memo FROM TABLE WHERE name = " + num
     Statement stmt = conn.credateStatement();
     ResultSet rst = stmt.executeQuery(sqlstr);
     
     특징
     
     SQL문을 수행하는 과정에서 매번 컴파일을 하게 때문에 성능상 이슈 발생
     
     실행되는 SQL 문을 확인 가능
     
     preparestatement
     
     예시
     
     String sqlstr = "SELECT name, memo FROM TABLE WHERE num = ?"
     PreparedStatement stmt = conn.preparedStatement();
     stmt.setInt(1, num);
     ResultSet rst = stmt.executeQuery(sqlstr);
     
     특징
     
     컴파일이 미리 되어있기 때문에 Statement에 비해 좋은 성능
     
     특수 문자를 자동으로 파싱해주므로 SQL Injection 같은 공격을 막을 수 있음
     
     '?' 부분에만 변화를 주어 쿼리문을 수행하므로 실행되는 SQL문을 파악하기 어려움
   
   preparestatement를 사용하면, 특수문자를 자동으로 escaping 해준다
   
   statement와는 다르게 쿼리문에서 전달인자 값을 ?로 받는 것
   
   서버 측에서 필터링 과정을 통해서 공격을 방어
   
   [[데이터베이스] Statement와 Prepared Statement](https://dheldh77.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-Statement%EC%99%80-Prepared-Statement)
   
   preparedstatement가 statement보다 안전한 이유
   
   Statement 객체에서 사용한 createStatement()라는 메소드
   
   이것을 사용할 경우 사용자의 입력 값을 미리 만들어 놓은 sql문에 적용한 후 컴파일을 하기 때문에 사용자의 입력 값에 따라 쿼리문의 형태가 바뀔 수 있어 보안에 취약
   
   사용자가 입력 값과 함께 'OR 1=1'과 같은 코드를 함께 전달할 경우 모든 사용자의 정보 등이 노출
   
   해결책으로 Statement 객체의 preparedStatement(query) 메소드를 사용
   
   이것은 미리 개발자가 작성한 쿼리문을 컴파일 하고 ?로 처리한 부분에 사용자의 입력 값을 넣기 때문에 쿼리문의 형태가 바뀌지 않아 보안성을 높일 수 있음
   
   [Statement 대신 preparedStatement 사용하는 이유](https://oper6210.tistory.com/157)
   
   언어별 PreparedStatement

4. Java, Python
   
   [[파이썬, Java] PreparedStatement SQL : 물음표 쿼리](https://knlg.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-Java-PreparedStatement-SQL-%EB%AC%BC%EC%9D%8C%ED%91%9C-%EC%BF%BC%EB%A6%AC)

5. C++
   
   [C++ preparedstatement](https://stackoverflow.com/questions/43015671/c-preparedstatement)

SQL Injection 테스트 사이트

[How to use SQLMAP to test a website for SQL Injection vulnerability - GeeksforGeeks](https://www.geeksforgeeks.org/use-sqlmap-test-website-sql-injection-vulnerability/)

간단 요약

1. [pictures](http://testphp.vulnweb.com/listproducts.php?cat=1)
   
   cat = 1 이 부분 → 값을 수정하여 사용자가 변경할 수 있는 GET 요청 매개 변수(cat = 1)
   
   잘못된 입력값으로 홈페이지에서 어떤 에러가 발생했는지 확인할 수 있음
   
   개발자가 방지를 하지 않은 상태

2. 명령어를 통해 사용 가능한 모든 데이터베이스를 탐색

3. 액세스하려는 데이터베이스의 이름을 지정

4. 데이터베이스에 액세스할 수 있게 되면 테이블에 액세스할 수 있는지 확인
   
   액세스 가능한 8 개의 테이블이 탐색

5. 이후 특정 열의 정보에 액세스할 수 있는 것들을 탐색

여기서도 preparedstatement를 사용하여 보안을 높이라고 설명

preparedstatement에서는 미리 쿼리문을 실행시켜놓고 사용자의 입력값을 받아서 실행

악성코드가 들어와도 실행문이 아니라 문자열로 인식

## ****저장 프로시저(Stored PROCEDURE)****

[저장 프로시저(Stored PROCEDURE) | 👨🏻‍💻 Tech Interview](https://gyoogle.dev/blog/computer-science/data-base/Stored%20PROCEDURE.html)

[[MySQL] 스토어드 프로시저(Stored Procedure) 기본](https://spiderwebcoding.tistory.com/7)

### 정의

일련의 쿼리를 마치 하나의 함수처럼 실행하기 위한 쿼리의 집합

여러 쿼리를 한 번에 수행하는 것

**특징**

1. SQL문법의 함수(Function)와 아주 유사
   
   함수(Function) : 클라이언트에서 처리, 리턴값 필수, 리턴값 하나만 반환가능
   
   [SQL 기본 함수](https://velog.io/@bahar-j/SQL)
   
   프로시저(Procedure) : 서버로 보내서 처리, 리턴값 선택, 리턴값 여러개 반환가능

2. 속도면에서는 프로시저가 더 빠른 성능
   
   프로시저 같은 경우 실행, 처리를 할 때 주로 사용
   
   함수는 간단한 계산이나 수치 결과를 나타낼 때 주로 사용

**사용해야 하는 이유**

1. 하나의 요청으로 여러 SQL문을 실행 가능
2. 네트워크 소요 시간을 줄일 수 있음(여러개의 쿼리를 처리하는 시점에서 네트워크 부하 줄임)
3. 보수성이 뛰어나다.
4. 개발 업무를 구분하여 개발할 수 있다. (DB관련 처리를 API처럼 만들어 제공)

### 장 / 단점

[[MSSQL]저장 프로시저 장단점, 사용 예제 정리](https://goldswan.tistory.com/51)

**장점**

1. 최적화 & 캐시
   
   프로시저의 최초 실행 시 최적화 상태로 컴파일이 되며, 그 이후 프로시저 캐시에 저장된다.
   
   만약 해당 프로세스가 여러 번 사용될 때, 다시 컴파일 작업을 거치지 않고 캐시에서 가져오게 된다.

2. 유지 보수
   
   작업이 변경될 때, 다른 작업은 건드리지 않고 프로시저 내부에서 수정만 하면 된다. (But, 장점이 단점이 될 수도 있는 부분이기도.. )

3. 보안
   
   프로시저 내에서 참조 중인 테이블의 접근을 막을 수 있다.

4. SQL문을 캡슐화하여 여러 곳에서 재사용
   
   프로시저를 사용해서 애플리케이션에서 여러 상황에 따라 해당 쿼리문이 필요할 때
   
   인자 값만 전달하여 쉽게 원하는 결과물을 받아낼 수 있다.
   
   트래픽 감소
   
   클라이언트가 직접 SQL문을 작성하지 않고, 프로시저명에 매개변수만 담아 전달하면 된다.
   
   SQL문이 서버에 이미 저장되어 있기 때문에 클라이언트와 서버 간 네트워크 상 트래픽이 감소된다.

5. 프로시저만 수정이 필요할 경우 애플리케이션을 배포하지 않고 프로시저만 배포하면 됨
   
   어플리케이션 코드 내에 SQL 로직이 포함되었을 경우 애플리케이션도 재배포 해야하지만
   
   프로시저 내에 포함될 경우 프로시저만 수정하여 배포하면 됩니다.

**단점**

1. 처리성능과 재사용면에서 좋지 않다
   
   구문 규칙이 SQL / PSM 표준과의 호환성이 낮기 때문에 코드 자산으로의 재사용성이 나쁘다.
   
   문자 또는 숫자 연산에서 프로그래밍 언어인 C나 Java보다 성능이 느리다.

2. 길게 작성된 프로시저의 경우 로직 파악이 어렵
   
   에러가 발생했을 때, 어디서 잘못됐는지 디버깅하는 것이 힘들 수 있다.

3. 배포 절차가 따로 없으므로 이력(버전)관리가 힘듦

4. 프로시저 내부에 연산이 포함될 경우 CPU 점유율이 높아지고 실행시간도 길어지므로
   
   LOCK이 걸려있을 경우 병목이 될 확률이 높아지게 됨

### 문법

[[MYSQL] 📚 스토어드 프로시저 & 스토어드 함수 사용법](https://inpa.tistory.com/entry/MYSQL-%F0%9F%93%9A-%EC%8A%A4%ED%86%A0%EC%96%B4%EB%93%9C-%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80-%F0%9F%94%B8-%EC%8A%A4%ED%86%A0%EC%96%B4%EB%93%9C-%ED%95%A8%EC%88%98#delimiter)

[프로시저 (Procedure)](https://tragramming.tistory.com/71)

1. 프로시저들 목록 확인
   
   ```sql
   show procedure status;
   ```

2. 프로시저 정의
   
   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/aa7eb9c9-1e4e-4c47-a01e-2633cb38f6fa/Untitled.png)
   
   ```sql
   CREATE OR REPLACE PROCEDURE 프로시저명(변수명1 IN 데이터타입, 변수명2 OUT 데이터타입) -- 인자 값은 필수 아님
   IS
   [
   변수명1 데이터타입;
   변수명2 데이터타입;
   ..
   ]
   BEGIN
   필요한 기능; -- 인자값 활용 가능
   END;
   
   EXEC 프로시저명; -- 호출
   ```
   
   ```sql
   -- DELIMITER는 프로시저 앞,뒤의 위치하여 안에 있는 부분은 한번에 실행될 수 있게 하는 역할을 한다.
   DELIMITER $$
   
   -- 프로시저 정의
   CREATE PROCEDURE search_user(IN txtValue CHAR(10), OUT outValue int) 
   #IN은 매개변수 입력값, out은 RETURN 같은 개념이다. 출력값                            
   
   -- 프로시저 실행 내용 정의
   BEGIN
      SELECT USER, HOST FROM MYSQL.USER;
   END $$
   
   DELIMITER;
   ```

3. 프로시저 호출
   
   ```sql
   CALL 프로시저명(매개변수들);
   ```

4. 프로시저 내용 조회
   
   ```sql
   **show create procedure 프로시저명;**
   ```

5. 프로시저 문법 구성
   
   1. 예시
      
      ```sql
      DROP PROCEDURE IF EXISTS calculate_grade;
      
      DELIMITER $$
      CREATE PROCEDURE calculate_grade(
      IN in_mid DOUBLE, 
      IN in_end DOUBLE,
      IN in_att INT,
      IN in_rep INT,
      IN in_class_num INT,
      IN in_student_num INT )
      -- 매개변수는 IN으로 가져온다.
      
      BEGIN
      -- 지역 변수 선언
      DECLARE total DOUBLE DEFAULT 0; -- double total = 0; 과 같다고 보면 된다.
      DECLARE grade VARCHAR(2);
      
      -- 변수 초기화
      SET total = in_mid + in_end + in_att + in_rep; -- 인자를 다 더한다.
      
      -- 분기
      IF total >= 95 AND total <= 100 THEN
          SET grade = 'A+';
      
      ELSEIF total >=90 AND total < 95 THEN
          SET grade = 'A';
      
      ELSEIF total >=85 AND total < 90 THEN
          SET grade = 'B+';
      
      ELSEIF total >=80 AND total < 85 THEN
          SET grade = 'B';
      
      ELSEIF total >=75 AND total < 80 THEN
          SET grade = 'C+';
      
      ELSEIF total >=70 AND total < 75 THEN
          SET grade = 'C';
      
      ELSEIF total >=65 AND total < 70 THEN
          SET grade = 'D+';
      
      ELSEIF total >=60 AND total < 65 THEN
          SET grade = 'D';
      
      ELSEIF total >=0 AND total < 60 THEN
          SET grade = 'F';
      END IF;
      
      -- 쿼리문
      UPDATE university.course
      SET
        course_mid = in_mid,
        course_end = in_end,
        course_report = in_rep,
        course_attendance = in_att,
        course_total = total,
        course_grade = grade
      WHERE course_student_num = in_student_num AND course_class_num = in_class_num AND course_num >= 1;
      
      END $$
      DELIMITER ;
      ```
      
      ```sql
      -- 프로시저 실행 (호출)
      CALL calculate_grade(40.0, 30.0, 9,9,1,2019160160);
      ```
      
      1. DELIMITER
      
      프로시저나 트리거에서 사용된다.
      
      프로시저를 생성할 때 프로시저 안에 있는 쿼리들이 ;으로 인해 실행되면 안되기 때문에 이를 막기 위해 DELIMITER를 이용하여 DELIMITER를 이용하여 지정된 문자가 나타나기 전까지는 ;을 만나도 실행되지 않게 막아준다.
      
      JAVA나 C++에서는 끝나는 부분에 **;**를 넣어서 끝을 알리는데
      
      그 역할을 DELIMITER가 대신 해준다
      
      2. IN / OUT
      
      in : 프로시저를 호출하기 위해 필요한 정보들로 함수의 매개변수(인자)에 해당한다.
      
      out : 함수의 반환값으로 이해하면 된다.
      
      3. DECLARE
      
      프로시저 내부에서 사용하는 지역 변수를 선언할 때 사용한다.
      
      4. SET
      
      변수의 값을 설정할 때 사용한다.
   
   2. IF 조건식 THEN 실행문 END IF
      
      ```sql
      DELIMITER $$
      
      CREATE PROCEDURE GetCustomerLevel(
        IN  p_customerNumber int(11), 
        OUT p_customerLevel  varchar(10))
      BEGIN
        DECLARE creditlim double;
      
        SELECT creditlimit INTO creditlim -- select한 결과 creditlimit 필드 값을 위에서 선언한 지역변수 creditlim에 넣는다 
        FROM customers
        WHERE customerNumber = p_customerNumber;
      
        IF creditlim > 50000 THEN
            SET p_customerLevel = 'PLATINUM';
        ELSEIF (creditlim <= 50000 AND creditlim >= 10000) THEN
            SET p_customerLevel = 'GOLD';
        ELSEIF creditlim < 10000 THEN
            SET p_customerLevel = 'SILVER';
        END IF;
      
      END$$
      
      DELIMITER ;
      ```
   
   3. while 문
      
      ```sql
      DELIMITER $$
      
      create procedure myProc()
      
      BEGIN
      declare i int;
      declare hap int;
      
      set i = 1;
      set hap = 0;
      
      myWhile: while (i<1000) do
        if (i % 3 = 0) then
          set i = i + 1;
          iterate myWhile; -- iterate == continue 같은 개념
        end if;
      
        set i = i + 1;
        set hap = hap + i;
      
        if (hap==900) then
            leave myWhile; -- leave == break 같은 개념
      
      end while;
      
      select hap;
      END $$
      
      DELIMITER ;
      ```

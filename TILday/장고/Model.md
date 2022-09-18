<Namespace>

1. URL_Namespace에 대한 설명으로 틀린 것은?
   
   1. URL_namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있다.

        2. app_name attribute를 작성해 URL namespace를 설정한다.

        3. app_name을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만         사용해야 한다. 

        4.URL 참조는 `/` 연산자를 사용하여 지정한다.

정답: 4. URL 참조는 `:`연산자를 사용하여 지정한다. (articles:index)

(추가) 2번 처럼 사용하지 않으면 NoReverceMatch 에러가 발생한다.

---

<Namespace>

2. Template namespace에 대한 설명으로 올바른 것은?

       1. Django는 기본적으로 프로젝트에 있는 모든 templates 파일을 찾을 수 있다.

       2. Template namespace는 Django temlplates의 기본 경로 자체를 변경할 방법이다.

       3. 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정해야 한다.

       4. 반드시 Template  namespace를 고려해야한다.

정답:   3.

오답: 

1.Django는 기본적으로 app_name/templates/ 경로에 잇는 templates 파일들만을 찾을 수 있다.

2.Django temlplates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것이다.

4.만약 단일 앱으로만 이루어진 프로젝트라면 상관없다.

---

<Database>

3. Database 기본 구조에 관한 설명 중 틀린 것은?

    1. 스키마는 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조로 '관계'라고도 부른다.

    2. 테이블은 필드와 레코드를 사용해 조직된 데이터 요소들의 집합이다.

    3. 각 필드에는 고유한 데이터 형식이 지정된다.

    4.  테이블의 데이터는 레코드에 저장된다.

정답: 2. 관계라고 불리는 것은 테이블이다.

---

<Database>

5. PK(Primary Key)와 쿼리(Query)에 대한 설명으로 틀린 것은?
   
   1. 쿼리는 데이터를 조회하기 위한 명령어를 일컬음.
   
   2. PK는 각레코드의 고유한 값으로 식별자로 사용된다.
   
   3. 쿼리는 주로 테이블형 자료구조에서 조건에 맞는 데이터를 추출하거나 조작하는 명령어로 사용된다.
   
   4. PK는 기술적으로 다른 항목과 중복되어 나타낼 수 있다.

    정답:  4 . PK는 기술적으로 다른 항목과 절대로 중복되어 나타날 수 없는 단일 값을 가진다.

---

<Model>

6. Model에 대한 설명으로 틀린 것은?
   
   1. 일반적으로 하나의 모델은 여러개의 데이터 베이스 테이블에 매핑된다.
   
   2. Model은  사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함한다.
   
   3. layout 구조이다.(저장된 데이터베이스의 구조)
   
   4. DJango는 Model을 통해 데이터에 접속하고 관리한다.

정답: 1. Model은 단일한 데이터에 대한 정보를 가지며 일반적으로 각각의 모델은 하나의 데이터 베이스 테이블에 매핑된다.

---

<Model>

7. Modle 이해하기

8. 모델 필드 알아보기.

---

<Migrations>

9. Migrations 관련 명령어에 대한 설명으로 올바른 것은?

        1. `python manage.py makemigrations` - 모델을 작성 혹은 변경한 것에 기반한 새로운         migration을 만들 때 사용

        2. `python manage.py migrate` - migrathion을 실제 db.sqlite3 DB 파일에 반영

        3.`python manage.py showmigrations` - migrations 파일들이 migrate 됐는지 여부를             확인하는 용도

        4. `python manage.py sqlmigrate articles 0001` - 해당 migrations 파일이 SQL         문 으로 어떻게 해석 될 지 미리 확인 할 수 있음

정답 : 1, 2, 3, 4

----

<ORM>

10. ORM에 대한 설명으로 틀린 것은?
    
    1. 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
    
    2. ORM의 장점으로는 SQL을 잘 알지 못해도 객체지향 언어로  DB 조작이 가능하다.
    
    3. ORM 장점으로는 ORM만으로 완전한 서비스를 구현 할 수 있다.
    
    4. ORM 장점으로는 객체 지향적 접근으로 인한 높은 생산성이 있다.

    정답: 3. ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음

---

<반드시 기억해야 할 migration 3단계>

1. models.py에서 변경사항이 발생하면

2. migrations 파일 생성(설계도 생성)
   
   - makemigrations

3. DB반영(모델과 DB의 동기화)
   
   - migrate

---

<추가필드 정의>

11. DateTimeField()에 대한 설명으로 올바른 것은?
    
    1. Python의 datetiome.datetiome 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드로 TimeField를 상속받는 클래스다.
    
    2. `auto_now`는 최초 생성 일자다.
    
    3. 선택 인자 `auto_now_add`는 Django ORM이 최초 insert시에만 현재 날짜와 시간을 갱신한다.
    
    정답: 3.
    
    오답: 1. DateField를 상속받는 클래스다.
    
              2. 최종 수정일자다. Django ORM이 save를  할 때마다 현재 날짜와 시간으로 갱신한다.

---

<QuerySet API 사전준비>

외부 라이브러리 설치 및 설정

1. 실습 편의를 위한 추가 라이브러리 설치및 설정.
   
   `pip install ipython`
   
   `pip install django-extensions`
   
   ```python
   #settings.py
   INSTALLED_APPS = [
       'articles',
       'django_extensions',
   ...,
   ]
   ```

2. 패키지 목록 업데이트
   
   `pip freeze > requirements.txt`

---

<Shell>

---

<QuerySet API>

12. Database API 구문에서 a, b, c, 가르키는 것을 적으세용

```pyhton
(a)Article.(b)objects.(c)all()
```

정답: (a)Model class, (b)Manager, (c)Queryset API

---

<QuerySet API>

13. QuerySet에 대한 설명으로 틀린 것은?
    
    1. 순회가 가능한 데이터로써 1개의 데이터를 불러와 사용할 수 있음
    
    2. Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음
    
    3. 'objects' manager를 사용하며 복수의 데이터를 가져오는  queryset method를 사용할 대 반환되는 객체
    
    4. 데이터베이스가 단일한 객체를 반환 할 때는 모델(Class)의 인스턴스로 반환된다.

정답: 1.  1개 이상의 데이터를 불러와 사용할 수 있다.

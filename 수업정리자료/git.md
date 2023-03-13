# Git

## 1. Git 초기 설정

### 작성자 설정 / 수정

```python
$ git config --global user.name "이름"
$ git config --global user.email "이메일"
```

### 작성자 설정 확인

```bash
$ git config --global --list
```

## 2. Git 기본

### git 폴더 설정

```bash
$ git init
```

### 파일의 현재 상태

```bash
$ git status
```

### add

```bash
# 현재 디렉토리에 속한 파일/폴더 전부
$ git add .

# 특정 파일
$ git add a.txt

# 특정 폴더
$ git add a 

# add 삭제
$ git reset HEAD 파일/폴더 # 특정 파일/폴더 add 삭제
$ git reset HEAD # 모든 파일/폴더 add 삭제
```

### commit

```bash
# commit
$ git commit -m "메시지"

# 마지막 1개의 commit 취소
$ git reset HEAD^

# 마지막 n개의 commit 취소
$ git reset HEAD~n

# commit message 변경
$ git commit --amend
```

### log

```bash
# 커밋 내용 조회
$ git log

# 커밋 내용 한 줄로 축약해서 조회
$ git log --oneline
```

## 3. Github 연결

### remote

```bash
# 원격 저장소 등록
$ git remote add 저장소이름 주소

# 원격 저장소 조회
$ git remote -v

# 원격 저장소 연결 삭제
$ git remote remove 저장소이름
```

### push

```bash
# 로컬 저장소에서 원격 저장소로 이동
$ git push 저장소이름 브랜치이름
```

### clone

```bash
# 원격 저장소의 커밋 내역을 가져와서, 로컬 저장소를 생성 (최초 1번)
$ git clone 저장소주소

# 원하는 이름으로 생성
$ git clone 저장소주소 원하는이름
```

### pull

```bash
# 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트
$ git pull 저장소이름 브랜치이름
```

### collision

```bash
# 로컬 커밋 기록과 원격 커밋 기록이 상충하여 발생하는 현상
# pull 후에 수정+저장+add+commit 하여 push
```

## 4. Example

```bash
# Day1 : 집(HOME)에서 깃허브(hub)로 push
# Day2 : 회사(company)에서 clone 생성 후 수정해서 깃허브로 push
# Day3 : 집에서 push 했던 기존 파일 수정한 뒤, git에서 수정된 파일 pull (collision) -> 해결 후 깃허브로 push

---

# Day1. 집에서 깃허브로 push

$ git init
$ git add.
$ git commit -m 'Day1 : 집에서 작성'
$ git remote add origin 'https://github.com/ysu6691'
$ git push origin master

---

# Day2. 회사(company)에서 pull & 수정 후 깃허브로 push

$ git clone 'https://github.com/ysu6691'

$ git add.
$ git commit -m 'Day2 : 회사에서 수정'
$ git push origin master

---

# Day3. 집에서 push 했던 기존 파일 수정한 뒤, git에서 수정된 파일 pull (collision) -> 해결 후 깃허브로 push

$ git add.
$ git commit -m 'Day3 : 집에서 재수정'
$ git pull origin master

# collision 발생
# 팀원과 상의 후 재수정

$ git add.
$ git commit -m 'Day3 : collision 해결'
$ git push origin master
```

---

# Gitlab에서 pull&push하기

## 처음부터 해당 브랜치만 pull 받아오고 싶을 때

1. git init
2. git remote add origin <깃 클론 링크>
3. git checkout -b <새로 생성할 브랜치명>
4. git pull origin <pull 받고싶은 상위 브랜치명>

## 새로운 브랜치에서 작업하고 푸시할 때[remote는 되어있음]

1. git checkout -b <새로 생성할 브랜치명 ex) feature/test>
   checkout -b : 브랜치 생성 및 스위치 변경
2. git pull origin <상위 브랜치명>git
3. 내용 수정.
4. git add .
5. gitmoji -c
6. git push origin feature/test
7. MR(머지 리퀘스트) feature/test -> 상위브랜치(fe or be)로 변경
8. MR(머지 리퀘스트) 수행
9. 머지 잘 됐는지 확인 후 팀원들에게 머지 알림

## 참고사항

- checkout -b 대신 switch -c를 최근에는 더 많이 사용한다고 합니다.

---

ex)

상위 폴더 pull 했을 때 아래와 같은 오류 뜬다면.

error : Please commit your changes or stash them before your merge.

→ 이거 뜨면 커밋 해줘야 된다

그래서

1. git add .
2. gitmoji -c

다음 pull을 다시 땡긴다.

그러면 충돌 난 부분을 볼 수 있을 텐데 그걸 수정하고 다시 push

중간 중간 status 확인



git lab에서 머지할 때 source branch 체크 제거하고 머지 하면 된다.

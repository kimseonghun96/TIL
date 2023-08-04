# **ARM : Advanced RISC Machine**

---

RISC를 기반으로 설계된 CPU 아키텍쳐

저전력, 고성능이 특징 (임베디드 기기)

```
**A**corn **R**ISC **M**achine

영국의 컴퓨터 회사 Acorn Computer가 제작한 CPU 아키텍쳐
```

## RISC 와 CISC

---

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/b037740e-ac9d-4e3c-aeab-e360e3032617/Untitled.png)

**CISC** (Complex Instruction Set Computer)

- 명령어의 형태와 크기가 복잡하지만 다양한 **가변 길이 명령어** 활용
- 상대적으로 적은 수의 명령어로도 프로그램을 실행할 수 있다.
- 컴파일 과정이 쉽고, 호환성이 좋다는 장점이 있지만 속도가 느리다.
- 명령어 크기, 실행시간이 일정하지 않다.

**RISC** (Reduced Instruction Set Computer)

- 명령어의 종류가 적고, 짧고 규격화된 명령어 사용
- 메모리 접근 최소화(load, store), 레지스터 활용 최대화
- 명령어 종류가 적기에, 더 많은 명령어로 프로그램 동작
- RISC보다 빠른 클럭으로 동작

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/5ff0432f-cccb-4ab4-8f76-3130a5644f66/Untitled.png)

<aside>
💡 `단순한 명령 집합을 가진 프로세서`가 `복잡한 명령 집합을 가진 프로세서`보다 훨씬 더 효율적이지 않을까?

</aside>

### **ARM 구조**

---

https://t1.daumcdn.net/cfile/tistory/25788C3550CAF8731A

ARM은 칩의 기본 설계 구조만 만들고, 실제 기능 추가와 최적화 부분은 개별 반도체 제조사의 영역으로 맡긴다.

따라서 물리적 설계는 같아도, 명령 집합이 모두 다르기 때문에 서로 다른 칩이 되기도 함

단순한 명령 집합 → 적은 수의 트랜지스터만 필요 → 간결한 설계와 더 작은 크기

명령 집합의 수가 적기 때문에 트랜지스터 수가 적고 이를 통해 크기가 작고 전원 소모가 낮은 ARM CPU가 스마트폰, 태블릿PC와 같은 모바일 기기에 많이 사용되고 있다.

### **ARM의 장점**

---

https://t1.daumcdn.net/cfile/tistory/1970603350CD96BC35

소비자에 있어 ARM은 '생태계'의 하나라고 생각할 수 있다. ARM을 위해 개발된 프로세서는 오직 ARM 프로세서가 탑재된 기기에서만 실행할 수 있다.

하지만, 하나의 ARM 기기에 동작하는 OS는 다른 ARM 기반 기기에서도 잘 동작한다.

이러한 장점 덕분에 수많은 버전의 안드로이드가 탄생하고 있으며 또한 HP나 블랙베리의 태블릿에도 안드로이드가 탑재될 수 있는 가능성이 생기게 된 것이다.

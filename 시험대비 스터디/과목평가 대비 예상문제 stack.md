##### 1.스택(stack)의 특성으로 올바른 설명을 고르시오. (3쪽)

    1. 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.

    2. 스택에 저장된 자료는 1대N의  관계를 갖는다.

    3.  스택에 자료를 꺼낼 수는 있지만 삽입할 수는 없다.

    4. 마지막에 삽입한 자료를 가장 마지막에 꺼낸다. 선입선출이라고 부른다.

    정답: 1

    오답 풀이:  2. 스택에 저장된 자료는 선형 구조를 갖는다. (자료간의 관계가 1대 1)

                       3. 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.

                       4. 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출이라고 부른다.   

---

##### 2. 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산에 대한 설명으로 틀린 것은? (4~5쪽 )

    1. 스택에서 마지막 삽입된 원소의 위치를 top 또는 stack pointer이라고 한다.

    2. 배열을 사용할 수 있다.

    3. 스택이 공백인지 아닌지를 확인하는 연산을 peek 라고 한다.

    4. 저장소 자체를 스택이라 부르기도 한다.

    정답: 3 - isEmpty다. (공백이면 True, 비어있지 않으면 False)

                    peek는 스택의 top에 있는 item(원소)을 반환하는 연산이다.

---

##### 3.  스택의 구현 문제

    1.

    2.

    3.

    4.

---

##### 4. function call 문제

    1.

    2.

    3.

    4.

---

##### 5. 피보나치 수를 구하는 재귀함수 중 a와 b에 들어갈 것으로 올바른 것은? (23쪽)

```python
def fibo(n) :
    if n < 2 :
        return n
    else :
        return fibo(a) + fibo(b)
```

    1. a: n     b: n -1 

    2. a: n     b: n+1

    3. a: n-1    b: n 

    4. a: n-1    b: n-2

    

    정답 : 4. n-1, n-2 (설명 추가 필요)

---

##### 6. 메모제이션(memoization)의 문제

    1.

    2.

    3.

    4.

---

##### 7. 피보나치 수 DP 적용 알고리즘 중 빈칸 a에 들어갈 것 메서드를 적으시오.

```python
def fibo2(n):
    f = [0, 1]


    for i in range(2, n+1)
        f.(a)(f[i-1] + fi[i-2)

    return f[n]
```

정답:

    정답: append

---

##### 8. 깊이 우선 탐색과 너비 우선 탐색을 올바르게 표현한 것을 고르세요

    1. 깊이 우선 탐색(Deepness First Search, DFS), 너비 우선 탐색(Width First Search, WFS)

    2. 깊이 우선 탐색(Depth First Search, DFS), 너비 우선 탐색(Breadth First Search, BFS)

    3. 깊이 우선 탐색(Deepness First Search, DFS), 너비 우선 탐색(Width First Search, WFS)

    4. 깊이 우선 탐색(Depth First Search, DFS), 너비 우선 탐색(Breadth First Search, BFS)

    정답: 2. 깊이 우선 탐색(Depth First Search, DFS), 너비 우선 탐색(Breadth First Search, BFS)

---

##### 9.

    1.

    2.

    3.

    4.

---

##### 10.

    1.

    2.

    3.

    4.

---

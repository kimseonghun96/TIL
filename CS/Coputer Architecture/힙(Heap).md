# **힙(Heap)**

---

- **완전 이진 트리**의 일종
  
  - Complete binary tree
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/98acc428-9e9f-4147-bc90-9363961fbb3f/Untitled.png)
    
    마지막 레벨을 제외하고, 트리가 모두 채워져 있음
    
    마지막 레벨은 왼쪽부터 오른쪽으로 채워져 있음

- **최대값** 또는 **최소값**을 빠르게 찾아내도록 만들어진 자료구조

- 반정렬 상태
  
  - 큰 값이 상위, 작은 값이 하위 레벨에 있음 ( 최대값 )

- 중복된 값 허용 ( 이진트리는 중복 허용x )

## 종류

---

### 최**대 힙(max heap)**

부모 노드의 키 값이 자식 노드의 키 값보다 **크거나 같은** 완전 이진 트리

### **최소 힙(min heap)**

부모 노드의 키 값이 자식 노드의 키 값보다 **작거나 같은** 완전 이진 트리

https://t1.daumcdn.net/cfile/tistory/17084F504DA9895214

## **구현**

---

- 힙을 저장하는 표준적인 자료구조는 `배열`
- 구현을 쉽게 하기 위해 배열의 첫번째 인덱스인 0은 사용되지 않음
- 노드 번호는 새로운 노드가 추가되어도 변하지 않음

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/ef73584e-4aba-49f7-bf80-c7b60768dc4b/Untitled.png)

### **부모 노드와 자식 노드 관계**

```cpp
왼쪽 자식 index = (부모 index) * 2

오른쪽 자식 index = (부모 index) * 2 + 1

부모 index = (자식 index) / 2
```

### **힙의 삽입**

---

1. 힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 **마지막 노드**에 삽입
2. 그 마지막 노드를 부모와 비교하면서, 필요시 교환하는 과정을 반복

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/f3e9c88f-5495-4a31-be3b-99efa17b1d20/Untitled.png)

부모 노드는 자신의 인덱스의 /2 이므로, 비교하고 자신이 더 크면 swap하는 방식

### **힙의 삭제**

---

1. 최대 힙에서 **최대값은 루트 노드**이므로 루트 노드가 삭제됨
2. 삭제된 루트 노드에는 힙의 **마지막 노드**를 가져옴
3. **자식 노드와 비교**를 반복하면서 재구성

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/7fd3a3e2-07c2-4fba-8af9-95af358279b5/Untitled.png)

## 우선순위 큐

---

<aside>
💡 우선순위의 개념을 queue에 도입한 자료구조

</aside>

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/a8023dce-11ac-49ef-922a-2f367bd64d93/Untitled.png)

- 언어별 priority queue
  
  ```cpp
  // java
  import java.util.PriorityQueue;
  import java.util.Collections;
  PriorityQueue<Integer> pq= new PriorityQueue<>();
  pq.add(1);
  a = pq.poll();
  
  // C++
  #include <queue>
  priority_queue<int> pq;
  pq.push(1);
  a = pq.top();
  pop()
  
  // python
  from queue import PriorityQueue
  pq= PriorityQueue()
  pq.put(1)
  a = pq.get();
  ```

**언제 사용?**

시뮬레이션 시스템, 작업 스케줄링, 수치해석 계산 등에 사용된다.

우선순위 큐는 배열, 연결리스트, 힙으로 구현

힙 → 삽입 : O(logn) , 삭제 : O(logn) (힙으로 구현이 가장 효율적!)

## 예상 질문

---

- 힙은 `완전 이진트리`입니다. `완전 이진트리`가 무엇일까요?
  
  - 마지막 레벨을 제외하고, 루트부터 차례대로 노드가 **모두** 채워진 이진 트리입니다.
  - 마지막 레벨은 **왼쪽부터 오른쪽**으로 채워져 있습니다.

- 힙을 사용하는 이유가 무엇일까요? 힙이 사용된 예시가 있을까요?
  
  - 힙은 최댓값 혹은 최솟값을 찾는 작업을 효율적으로 수행하는 자료구조입니다.
  - 트리의 균형이 잡혀 있다면 시간 복잡도 O(logN)으로 최댓값 혹은 최솟값을 찾을 수 있습니다.
  - 따라서 이 부분을 활용할 수 있는 `실시간 급상승 검색어 제공 서비스` 등에서 사용됩니다.
  - 시뮬레이션 시스템, 작업 스케줄링, 수치해석 계산

- 힙과 관련된 `시간복잡도`에 대해 말씀해 주세요.

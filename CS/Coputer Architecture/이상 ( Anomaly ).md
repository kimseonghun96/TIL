# 이상 ( Anomaly )

---

<aside>
💡 테이블을 설계할 때 잘못 설계하여 데이터를 삽입, 삭제, 수정할 때 논리적으로 생기는 오류

</aside>

- 데이터들이 불필요하게 **중복**되어 릴레이션 조작에 예기치 못한 문제 발생

- 속성들의 종속관계를 하나의 릴레이션에 표현하기 때문에 발생

- 정규화를 거치지 않은 데이터베이스에서 발생할 수 있는 현상

- **정규화**를 통해서 이상 현상을 제거 할 수 있다.

## **삽입 이상 (Insertion Anomaly)**

---

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/1328033a-0316-4775-a9cd-f875560df242/Untitled.png)

> 자료를 삽입할 때 의도하지 않은 자료까지 삽입해야만 자료를 테이블에 추가가 가능한 현상

- 새로운 성에 NULL 값이 들어가거나, 불필요한 데이터를 추가해야 하는 상황

```
![Untitled](<https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/bbd0a222-ad8e-4554-909c-5e2be8b74126/Untitled.png>)
```

## **갱신 이상 (Update Anomaly)**

---

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/8f9c3412-e78e-4f7c-af98-9e3a5e578856/Untitled.png)

> 중복된 데이터 중 일부만 수정되어 데이터 모순이 일어나는 현상

- 일부만 수정되어, 데이터가 불일치

```
![Untitled](<https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/32b6c97e-1f3c-4113-9aeb-280bcff1ac52/Untitled.png>)
```

## **삭제 이상 (Deletion Anomaly)**

---

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/beeffe74-f486-4274-8c2c-6637918b3084/Untitled.png)

> 어떤 정보를 삭제하면, 의도하지 않은 다른 정보까지 삭제되어버리는 현상

- 튜플 삭제로 인해 꼭 필요한 데이터까지 함께 삭제

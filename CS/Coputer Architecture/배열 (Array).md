# 배열 (Array)

# 배열 회전

## 기본 회전 알고리즘

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/ceeff79b-6e79-449b-980e-a3e78101df68/Untitled.png)

```jsx
void leftRotatebyOne(int arr[], int n){
    int temp = arr[0], i;
    for(i = 0; i < n-1; i++){
       arr[i] = arr[i+1];
    }
    arr[i] = temp;
}

// 회전 수 만큼 돌리는 것 보다 효율적일 것 같아서 추가
void leftRotatebyN(int arr[], int n, int N){
    int temp[] = new int[N], i, j;
        for(j = 0; j < N; j++){
       temp[i] = arr[i];
    }
    for(i = 0; i < n-N; i++){
       arr[i] = arr[i+N];
    }
        for(j = i; j < n; j++){
       arr[k] = temp[j-i];
    }
}
```

## 저글링 알고리즘

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/508e4892-0806-4de8-bdcd-6846439ea664/d302fb60-adae-44a0-b28e-fe1a605e7efe/Untitled.png)

```cpp
#include  
using namespace std; 

// 최대공약수 gcd 활용
int gcd(int a, int b) 
{ 
    if (b == 0) 
        return a; 

    else
        return gcd(b, a % b); 
} 

// n : 전체 길이, d : 회전 횟수
void leftRotate(int arr[], int d, int n) 
{ 
    for (int i = 0; i < gcd(d, n); i++) { 

        int temp = arr[i]; 
        int j = i; 

        while (1) { 
            int k = j + d; 
            if (k >= n) 
                k = k - n; 

            if (k == i) 
                break; 

            arr[j] = arr[k]; 
            j = k; 
        } 
        arr[j] = temp; 
    } 
} 

void printArray(int arr[], int size) 
{ 
    for (int i = 0; i < size; i++) 
        cout << arr[i] << " "; 
} 

int main() 
{ 
    int arr[] = { 1, 2, 3, 4, 5, 6, 7 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 

    // Function calling 
    leftRotate(arr, 2, n); 
    printArray(arr, n); 

    return 0; 
}
```

## 역전 알고리즘

```cpp
#include <iostream>
using namespace std;

// swap을 활용한 reverse 구현
void reverseArr(int arr[], int start, int end){

    while (start < end){
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }
}

// d로 나눠서 역전 알고리즘 수행
void rotateLeft(int arr[], int d, int n){
    reverseArr(arr, 0, d-1);
    reverseArr(arr, d, n-1);
    reverseArr(arr, 0, n-1);
}

void printArray(int arr[], int n){
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
}

int main(void){

    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int n = sizeof(arr) / sizeof(arr[0]);
    int d = 3;

    rotateLeft(arr, d, n);
    printArray(arr, n);

    return 0;
}
```

# 배열의 특정 최대 합 구하기

```cpp
// 지정된 배열에서 하나씩 회전을 해서 i*arr[i]의 합이 가장 컸을 때 값을 출력하는 문제

#include <iostream>
using namespace std;

int maxVal(int arr[], int n){

    int arrSum = 0; // arr[i]의 전체 합
    int curSum = 0; // i*arr[i]의 전체 합

    for(int i = 0; i < n; i++){
        arrSum = arrSum + arr[i];
        curSum = curSum + (i*arr[i]);
    }

    int maxSum = curSum;

    for (int j = 1; j < n; j++){
        curSum = curSum + arrSum - n*arr[n-j];

        if ( curSum > maxSum )
            maxSum = curSum;
    }

    return maxSum;

}

int main(void){

    int arr[] = {1,20,2,10};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << maxVal(arr, n);

    return 0;
}
```

# 특정 배열을 arr[i] = i로 재배열 하기

```cpp
#include <iostream>
using namespace std;

{-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}

int fix(int A[], int len){

    for(int i = 0; i < len; i++) {

        if (A[i] != -1 && A[i] != i){ // A[i]가 -1이 아니고, i도 아닐 때

            int x = A[i]; // 해당 값을 x에 저장

            while(A[x] != -1 && A[x] != x){ // A[x]가 -1이 아니고, x도 아닐 때

                int y = A[x]; // 해당 값을 y에 저장
                A[x] = x; 

                x = y;
            }

            A[x] = x;

            if (A[i] != i){
                A[i] = -1;
            }
        }
    }

}

void printArray(int A[], int len){
    for(int i = 0; i < len; i++){
        cout << A[i] << " ";
    }
}

int main() {

    int A[] = { -1, -1, 6, 1, 9, 
                3, 2, -1, 4, -1 };

    int len = sizeof(A) / sizeof(A[0]);
    fix(A, len);
    printArray(A, len);

    return 0;
}
```

## 면접 질문

### 💡 **Array(List)의 가장 큰 특징과 그로 인해 발생하는 장점과 단점에 대해 설명해주세요.**

Array의 가장 큰 특징은 순차적으로 데이터를 저장한다는 점입니다.

데이터에 순서가 있기 때문에 0부터 시작하는 index가 존재하며, index를 사용해 특정 요소를 찾고 조작이 가능하다는 것이 Array의 장점입니다.

순차적으로 존재하는 데이터의 중간에 요소가 삽입되거나 삭제되는 경우 그 뒤의 모든 요소들을 한 칸씩 뒤로 밀거나 당겨줘야 하는 단점도 있습니다.

이러한 이유로 Array는 정보가 자주 삭제되거나 추가되는 데이터를 담기에는 적절치 않습니다.

### 💡 **Array를 적용시키면 좋을 데이터의 예를 구체적으로 들어주세요. 구체적 예시와 함께 Array를 적용하면 좋은 이유, 그리고 Array를 사용하지 않으면 어떻게 되는지 함께 설명해주세요.**

Array를 적용시키면 좋은 예로 주식 차트가 있습니다.

주식 차트에 대한 데이터는 요소가 중간에 새롭게 추가되거나 삭제되는 정보가 아니며, 날짜별로 주식 가격이 차례대로 저장되어야 하는 데이터입니다.

즉, 순서가 굉장히 중요한 데이터이므로 Array 같이 순서를 보장해주는 자료구조를 사용하는 것이 좋습니다.

Array를 사용하지 않고 순서가 없는 자료 구조를 사용하는 경우에는 날짜별 주식 가격을 확인하기 어려우며 매번 전체 자료를 읽어 들이고 비교해야 하는 번거로움이 발생합니다.

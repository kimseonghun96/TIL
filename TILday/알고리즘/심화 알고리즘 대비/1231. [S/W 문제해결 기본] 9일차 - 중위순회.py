'''
1. 각 테스트 케이스마다 0으로 초기화 된 (n + 1) 크기의 data 리스트를 정의한다.

2. 각 정점 정보를 입력받아 data[i+1]에 1번째 값(temp[1]을 할당한다.

3. 해당 테스트 케이스 번호를 출력하고, in_order() 함수를 호출하여 문제에서 요구하는 정점의 알파벳을 출력한다.

4. in_order() 함수의 작업은 아래와 같다.
  - 전달받은 value 값이 n 이하일 경우 value * 2를 매개변수로 하여 in_order() 함수를 재귀 호출한다. (왼쪽 자식 정점)
  - data[value] 값을 출력한다.
  - value * 2 + 1을 매개변수로 하여 in_order() 함수를 재귀 호출한다. (오른쪽 자식 정점)
'''


def in_order(value) :
    if value <= n :
        in_order(value * 2)
        print(data[value], end='')
        in_order(value * 2 + 1)


for tc in range(1, 11) :
    n = int(input())
    data = [0] * (n + 1)
    for i in range(n) :
        temp = list(input().split())
        data[i+1] = temp[1]

    print('#%d' % tc, end=' ')
    in_order(1)
    print()
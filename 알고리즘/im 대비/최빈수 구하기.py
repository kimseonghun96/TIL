T = int(input())
for tc in range(1, T+1):
    testcase = int(input())
    arr = list(map(int, input().split()))
    temp = [0] * (len(arr)+1)    # 인덕스 저장할 공간 +1 하는 이유는 0번째 인덱스 사용x


    for i in arr:
        temp[i] += 1   # 인덱스에 해당하는 수가 나올 때마다 +1


    max_temp = max(temp)  # 가장 큰 수의 인덱스
    result = []
    for i in range(len(temp)):
        if temp[i] == max_temp: # 인덱스의 값과 가장 큰 값이 같다면
            result.append(i)    # 결과 값에 추가

    print(f'#{testcase} {max(result)}')
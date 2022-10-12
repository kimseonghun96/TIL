switch = int(input())  # tmdnlcl
arr = list(map(int, input().split()))

N = int(input())
for i in range(N):
    gender, number = map(int, input().split())
    man_number = []
    for i in range(1, len(arr)):
        if i % 3 == 0:
            man_number.append(i-1)

    # print(man_number)
    number = number - 1

    if gender == 1:
        for t in range(len(man_number)):
            if 0 <= man_number[t]:
                if arr[man_number[t]] == 1:
                    arr[man_number[t]] = 0

                elif arr[man_number[t]] == 0:
                    arr[man_number[t]] = 1

    if gender == 2:
        if 0 <= arr[number]:
            if arr[number] == 1:
                arr[number] = 0

            elif arr[number] == 0:
                arr[number] = 1

            for k in range(len(arr)):
                if 0 <= number+k < len(arr) and 0 <= number - k < N:

                    if arr[number-k] == arr[number+k]:
                        if arr[number-k] == 1 and arr[number+k] == 1:
                            arr[number-k] = 0
                            arr[number+k] = 0

                        elif arr[number-k] == 0 and arr[number+k] == 0:
                            arr[number-k] = 1
                            arr[number+k] = 1

# 일단 스위치 개수 받고, 20의 배수니?
for t in range(switch):  # 0,1,2,3...7 인덱스
    print(arr[t], end=' ')
    if (t + 1) % 20 == 0:  # 스위치 숫자
        print()



'''
T = int(input())
light = list(map(int, input().split()))
students = int(input())
for _ in range(students):
    gender, number = map(int, input().split())

    # 남학생 - 스위치 idx에서 number의 배수인 것들의 상태를 바꿔
    if gender == 1:
        # 스위치 번호 중에서 number(3)의 배수인 것을 찾아
        idx_n_m = []
        for i in range(1, len(light) + 1):  # 1 2 ... 8
            if i % number == 0:
                idx_n_m.append(i)  # [3,6]

        # 그 인덱스들의 상태를 바꿔줘 
        for idx in idx_n_m:  # 3, 6 
            if light[idx - 1] == 0:
                light[idx - 1] = 1
            else:
                light[idx - 1] = 0  # [0, 1, 1, 1, 0, 1, 0, 1]

    # <여학생 - 자기가 받은 수와 같은 번호가 붙은 스위치의 좌우 대칭 확인>
    # 같아? 그 범위 내에 있는 모든 수를 바꿔 자기 번호까지
    # 달라? 자기 번호만 바꿔

    # 어쨌든 자기 번호는 바뀜
    else:
        g_idx = number - 1  # 자기가 받은 수의 스위치 인덱스
        if light[g_idx] == 1:
            light[g_idx] = 0
        else:
            light[g_idx] = 1

        # 좌우 확인
        scope = 1
        while True:
            if 0 <= g_idx - scope and g_idx + scope <= len(light) - 1 and light[g_idx - scope] == light[g_idx + scope]:
                if light[g_idx - scope] == 1:
                    light[g_idx - scope] = light[g_idx + scope] = 0
                else:
                    light[g_idx - scope] = light[g_idx + scope] = 1
                scope += 1
            else:
                break

            # 한 줄에 20개씩, 21부턴 아래에
# 일단 스위치 개수 받고, 20의 배수니?
for t in range(T):  # 0,1,2,3...7 인덱스
    print(light[t], end=' ')
    if (t + 1) % 20 == 0:  # 스위치 숫자
        print()'''
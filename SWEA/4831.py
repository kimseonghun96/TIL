# 전기버스
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())             # 충전 횟수(K), 종점(N), 충전기(M)
    chargers = list(map(int, input ().split()))     # 충전기에 대한 정보를 받음(위치)

    bus = K                                         # 버스의 처음 충전된 상태
    stations = [0]*(N+1)                            # 정류장의 수를 1차원 리스트 형태로 나타냄

    for charger in chargers:                        # 충전기의 정보 안에서 충전기를
        stations[charger] = 1                       # 충전기 위치를 리스트 안에 1로 표시

    answer = 0                                      # 최소 충전횟수
    prev_location = 0                               # 전 정류장 정보

    while bus < N:                                  # 버스를 종점까지 달림
        if stations[bus] == 1:                      # 버스가 충전기를 만나면
            prev_location = bus                     # 전 정류장에 버스 정보 입력하고
            bus += K                                # 버스를 충전된 상태로 다시 만듬
            answer += 1                             # 충전 횟수 1 증가

        else:                                       # 충전기 안만나면
            bus -= 1                                # 버스의 직전 정류장을 본다.
            if prev_location == bus:                # 버스가 전 정류장 즉 0이 되면
                answer = 0                          # 충전 횟수 0
                break                               # 멈춰여ㅛ

    print(f'#{tc} {answer}')


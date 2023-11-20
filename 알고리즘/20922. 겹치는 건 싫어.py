# 수열의 시작과 마지막 인덱스 값을 갖는 start, end 변수의 초기값은 0으로 초기화 한다.
# start 인덱스부터 end 인덱스까지 해당하는 부분 수열이 K 개 이상의 중복이 없는지 검사한다.
# 검사 방법은 end 의 값을 증가시키면서 end 인덱스에 해당하는 숫자의 개수를 증가시킨다.
# 만약 end 인덱스에 해당하는 숫자의 개수가 K 를 넘는다면 end 의 진행은 중단시키고 start 의 값을 증가시키면서 start 인덱스에 해당하는 숫자의 개수를 감소시킨다.
# start 의 값을 증가하는 중 end 인덱스에 해당하는 숫자의 개수가 K 와 같아진다면 다시 end 의 값을 증가시키는 연산을 반복한다.
# 각 단계에서 answer를 업데이트하여 가장 긴 부분 수열의 길이를 구합니다.


import sys
from collections import defaultdict

def solution(N, K, A):
    answer = 0
    start, end = 0, 0

    # [1] 수열에 주어진 각 정수의 개수
    numberCount = defaultdict(int)


    # [2] 투 포인터
    while end < N:
        if numberCount[A[end]] >= K:
            numberCount[A[start]] -= 1
            start += 1
        else:
            numberCount[A[end]] += 1
            end += 1
            answer = max(answer, end - start)

    return answer

# input
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

# result
result = solution(N, K, A)
print(result)
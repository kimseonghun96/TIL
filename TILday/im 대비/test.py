import sys
sys.stdin = open('test_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # print(arr)

    row_list = []
    for r in range(3):
        temp_list = []
        for c in range(3):





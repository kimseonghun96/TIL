# 주어진 문장의 인댁스를 비교해서
# 공통되는 부분을 그냥 출력 틀린 부분은 ? 로 출력하면 되는 부분
# 가장 처음걸 비교 문장으로 만들고 그 이후의 것을
# 비교하면서 바꾸자
N = int(input())

# 비교 문장
sentence = list(input())

for i in range(N - 1):
    test_sentence = list(input())
    for j in range(len(sentence)):
        if sentence[j] !=  test_sentence[j]:
            sentence[j] = '?'


print(''.join(sentence))

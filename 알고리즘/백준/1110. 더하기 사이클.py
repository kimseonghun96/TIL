'''
4
1 2 3 4 5 6
'''

def solution(numlist, n):
    answer = []
    for i in numlist:
        result = i - n
        if result < 0:
            result *= -1
        answer.append((result, i))

        answer.sort(key = lambda x :(x[0], -x[1]))

    answer2 = []
    for i in answer:
        answer2.append(i[1])

    return answer2

# 받은 수를 쪼개서 리스트로 만든 후
# 포문을 돌면서 앞 뒤 인덱스가 같은 지 비교
# 앞 뒤 인덱스가 틀리면 no


while True:
    n = input()

    if n == '0':
        break

    n_list = list(n)
    is_palindrome = True
    for i in range(len(n_list) // 2):
        if n_list[i] != n_list[-i - 1]:
            is_palindrome = False
            break

    if is_palindrome:
        print('yes')
    else:
        print('no')





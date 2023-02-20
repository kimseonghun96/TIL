# def add(a, b):
#     print('함수의 결과 :',a + b)
#
#
# add(3, 7)
#
#
# #  글로벌 함수   지역 변수와 글로벌 변수는 같은 이름의 지역 변수가 있을 경우 먼저 적용 된다.
# a = 10
# def func():
#     global a
#     a += 1
#     print(a)
#
# func()

def operator(a, b):
    add_var = a+b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var,divide_var # 반환된 순서에 따라 함수에 담을 수 있다.


a, b, c, d = operator(3, 7)

print(a, b, c, d)
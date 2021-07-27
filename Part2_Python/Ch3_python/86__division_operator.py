
'''
division operator
: 5 // 3 은 int(5 / 3) 과 동일
: 정수형 결과가 필요한 나눗셈 연산에서는 항상 // 연산자 사용

divmod
: 몫과 나머지 동시에 구함
'''


# division operator
print(5 / 3)  # 1.6666666666666667
print(type(5 / 3))  # <class 'float'>

print(int(5 / 3))  # 1
print(type(int(5 / 3)))  # <class 'int'>

print(5//3)  # 1
print(type(5//3))  # <class 'int'>


# divmod
print(divmod(5, 3))  # (1, 2)

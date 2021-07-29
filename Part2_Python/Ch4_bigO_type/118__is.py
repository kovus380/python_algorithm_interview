

'''
비교 연산자 is ==
is - id() 값 비교 함수
   - none 은 null로서 값 자체가 정의되어 있지 않음
     -> == 으로 비교불가함
     -> is로만 비교 가능
'''


import copy

a = None
print(a is None)  # True

a = [1, 2, 3]
print(a == a)  # True
print(a == list(a))  # True

print(a is a)  # True
print(a is list(a))  # False

print(a, list(a))  # [1, 2, 3] [1, 2, 3]
print(id(a), id(list(a)))  # 2843894686144 2843894823552

print(a == copy.deepcopy(a))  # True
print(a is copy.deepcopy(a))  # False

print(a, copy.deepcopy(a))  # [1, 2, 3] [1, 2, 3]
print(id(a), id(copy.deepcopy(a)))  # 2843894686144 2843894823552

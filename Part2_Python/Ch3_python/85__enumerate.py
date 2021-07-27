
'''
enumerate
: 여러 가지 자료형 (list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴
'''


a = [1, 2, 3, 2, 45, 2, 5]

print(enumerate(a))
# <enumerate object at 0x00000287CBD73BC0>

print(list(enumerate(a)))
# [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]


# 리스트의 인덱스와 값을 함께 출력하는 방법

# 1
# 불필요한 a[i] 및 전체 길이 조회 -> 깔끔하지 않음
for i in range(len(a)):
    print(i, a[i])

# 2
# 변수를 별도로 관리 -> 깔끔하지 않음
i = 0
for v in a:
    print(i, v)
    i += 1

# 3
# enumerate 이용 -> 가장 깔끔
for i, v in enumerate(a):
    print(i, v)
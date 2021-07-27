
'''
range
: 제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성
: 이전 파이썬에서는 숫자를 미리 생성해서 리스트로 리턴하는 방식
: --> list(range(x))
: 제너레이터를 리턴하듯  range 클래스만 리턴함
'''

import sys

# 숫자 100만 개를 생성하는 방법
a = [n for n in range(1000000)]  # a에는 이미 생성된 값이 담겨 있음
b = range(1000000)  # 생성해야 한다는 조건만 존재

print(len(a))  # 1000000
print(len(b))  # 1000000
print(len(a) == len(b))  # True

print(b)  # range(0, 1000000)
print(type(b))  # <class 'range'>

# 메모리 점유율 비교
# 100만 개가 아니라 1억 개라도 b 변수의 메모리 점유율은 동일 -
# > 생성 조건만 보관하고 있기 때문
print(sys.getsizeof(a))  # 8697456
print(sys.getsizeof(b))  # 48

# 인덱스로 접근 시에는 바로 생성하도록 구현되어 있음
# 리스트와 거의 동일한 느낌으로 사용 가능
print(b[999])


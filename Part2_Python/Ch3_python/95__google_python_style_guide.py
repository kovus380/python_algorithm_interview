

'''
- 함수의 기본 값으로 객체 사용 하면 안 됨
- True False 판별시 암시적인 방법 사용
- 정수값 비교시에는 직접 비교하기
- 최대 줄 길이는 80자
'''

# 함수의 기본 값으로 가변 객체 사용하면 안 됨
# NO
from typing import Optional, Sequence, Mapping

def foo(a, b=[]):
    pass

def foo(a, b: Mapping = {}):
    pass


# YES
def foo(a, b=None):
    pass

def foo(a, b: Optional[Sequence] = None):
    pass


# True, False 판별시 암시적인 방법 사용
users = []

# YES
if not users:
    pass

# NO
if len(users) == 0:
    pass


# 정수를 처리할 때는 값을 직접 비교하는 편이 덜 위험하다
baby = 100

# YES
if baby == 0:
    pass

if baby % 10 == 0:
    pass

# NO
if baby is not None and not baby:
    pass

if not baby % 10:
    pass



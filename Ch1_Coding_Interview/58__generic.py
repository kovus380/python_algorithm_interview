'''
파이썬 - 동적 타이핑 언어 -> 제네릭 필요 없음
코드 복잡도 높아질 수록 혼란을 가중시킴
'''

def are_equal(a, b):
    return a == b


print(are_equal(10, 10.0)) # True

'''
타입 명시 -> 가독성 좋아짐, 버그 발생 확률 줄임 
'''

from typing import TypeVar


T = TypeVar('T')
U = TypeVar('U')


def are_equal(a: T, b: U) -> bool:
    # (변수명: 변수 타입) -> 리턴 타입
    print(type(a)) # int
    print(type(b)) # float
    return a == b

print(are_equal(10, 10.0)) # True


# 함수 타입 지정 예제
def print_len(n: int) -> int:
    return(len(n))


n = input()
print(print_len(n))
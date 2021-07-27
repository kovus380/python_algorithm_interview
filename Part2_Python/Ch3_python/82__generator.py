'''
generator
: 루프의 반복 동작을 제어할 수 있는 루틴 형태
: 제너레이터를 이용하면 제너레이터만 생성해두고 필요할 때 언제든 숫자를 만들어낼 수 있다
'''

# 1
# yield 구문을 사용하면 제너레이터 리턴할 수 있음
# yield 구문 사용하여 제네레이터
# yield 는 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


g = get_natural_number()

print(type(get_natural_number()))  # <class 'generator'>
print(g)  # <generator object get_natural_number at 0x000001EFA70B9C10>


# 다음 값을 생성하려면 next()로 추출
g = get_natural_number()
for _ in range(0, 100):
    print(next(g))  # 1 2 3 ... 100



# 2
# 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능
def generator():
    yield 1
    yield 'string'
    yield True


g = generator()
print(g)  # <generator object get_natural_number at 0x000001EFA70B9C10>

print(next(g))  # 1
print(next(g))  # string
print(next(g))  # True
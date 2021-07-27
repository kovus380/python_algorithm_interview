'''
리스트 컴프리헨션
- 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문
- 람다 표현식에 map이나 filter를 섞어서 사용하는 것엥 비해 가독성 좋음
- 표현식 2개 넘지 않도록 (가독성 측면)
'''



# 1
# lambda 인자: 표현식
print(list(map(lambda x: x+10, [1,2,3])))  # [11, 12, 13]
print((lambda x,y: x + y)(10, 20))  # 30



# 2
# 홀수인 경우 2를 곱해 출력하라
# 리스트 컴프리헨션 이용
a = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1] # [2, 6, 10, 14, 18]

# 리스트 컴프리헨션 이용하지 않았을 때
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)
print(a)  # [2, 6, 10, 14, 18]



# 3
# 딕셔너리에도 적용 가능
original = {'pizza':'italy', 'kimchi':'korea'}

# 리스트 컴프리헨션 이용
a = {key: value for key, value in original.items()}
print(a)  # {'pizza': 'italy', 'kimchi': 'korea'}

# 리스트 컴프리헨션 이용하지 않았을 때
b = {}
for key, value in original.items():
    b[key] = value
print(b)  # {'pizza': 'italy', 'kimchi': 'korea'}

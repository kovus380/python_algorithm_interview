'''
람다 사용하지 않고 두 번째 이후 키 정렬 후 첫 번째 키 정렬하는 함수
'''

def func(x):
    return x.split()[1:], x.split()[0]

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

logs.sort(key=func)
print(logs)
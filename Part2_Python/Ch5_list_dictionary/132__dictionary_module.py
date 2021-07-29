

# defultdict
# 존재하지 않는 키를 조회할 경우, 에러 메세지 출력 대신
# 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성
import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a)  # defaultdict(<class 'int'>, {'A': 5, 'B': 4})
print(type(a))  # <class 'collections.defaultdict'>

a['C'] += 1
print(a)  # defaultdict(<class 'int'>, {'A': 5, 'B': 4})

print(a['D'])  # 0

b = collections.defaultdict(str)
print(b['t']+'a')  # a
print(len(b['k']))  # 0


# Counter 객체
# 아이템에 대한 개수를 계산해 딕셔너리로 리턴
# 키에는 아이템의 값이 값에는 아이템의 개수가 들어간 딕셔너리 생성
aa = [1, 2, 3, 4, 5, 5, 5, 6, 6]
bb = collections.Counter(aa)  # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
print(bb)
print(type(bb))  # <class 'collections.Counter'>

# Counter 객체에서 가장 빈도 수가 높은 요소 추출 -> most_common 사용
print(bb.most_common(2))  # [(5, 3), (6, 2)]


# OrderedDict 객체
# 해시 테이블은 입력 순서에 관여하지 않는 자료형
c = collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1})
print(c)  # OrderedDict([('banana', 3), ('apple', 4), ('pear', 1)])

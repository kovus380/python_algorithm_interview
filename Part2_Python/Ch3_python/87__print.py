
# 콤마(,)로 구분
# 한 칸 공백이 디폴트
print('A1', 'B1')  # A1 B1


# sep 파라미터로 구분자 지정할 수 있음
print('A1', 'B1', sep=',')  # A1,B1


# print() 함수는 항상 줄바꿈
# end 파라미터를 공백으로 처리하면 줄바꿈 하지 않도록 제한
print('aa', end=' ')
print('bb')  # aa bb


# 리스트 출력시 join 으로
a = ['A', 'B']
print(' '.join(a))  # A B


# idx 값에 1을 더해서 fruit과 함께 출력
idx = 1
fruit = 'Apple'

# 1
print('{0}: {1}'.format(idx + 1, fruit))  # 2: Apple

# 2
print('{}: {}'.format(idx + 1, fruit))  # 2: Apple

# 3
# f-string - 가장 선호
# 간결, 직관, 빠름
print(f'{idx + 1}: {fruit}')  # 2: Apple

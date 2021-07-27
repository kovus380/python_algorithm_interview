'''
1부터 10까지의 합을 구하는 루프 구조
'''

# 1
sum1 = 0
for i in range(1, 10+1):
    sum1 += i
print(sum1)

# 2
sum2 = sum(i for i in range(1, 10+1))
print(sum2)

# 3
print(sum(range(1, 10+1)))
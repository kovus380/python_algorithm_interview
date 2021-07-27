# 들여쓰기는 공백 4칸이 원칙

# 첫 번쨰 줄에 파라미터가 있다면 파라미터가 시작되는 부분에 맞춤
foo = max(111111, 222222,
          333333, 444444)

# 첫 번째 줄에 파라미터가 없다면 공백 4칸 추가 입력
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

print(
    111111, 222222,
    333333, 444444)




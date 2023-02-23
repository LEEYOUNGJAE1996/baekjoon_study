# 230223
# N을 입력 받은 후 N단의 구구단 출력 1~ 9까지

N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")

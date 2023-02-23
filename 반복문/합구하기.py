# 230223
# n이 주어진 경우 1~n 까지의 합 구하기
n = int(input())

sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

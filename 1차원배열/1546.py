# 230302


n = int(input())
l = []
max = 0
# map의 경우 각 분리된 값들에 첫 번째를 인자를 실행하는 것!
l = list(map(int, input().split()))
for i in range(n):
    if max < l[i]:
        max = l[i]
# 최대값 구하기 result = max(l)
# 새로운 값을 대입
# 평균값을 구하기 위한  sum
sum = 0
for i in range(n):
    l[i] = l[i]/max*100
    sum += l[i]
# sum 한 번에  result = sum(l)
print(sum/n)

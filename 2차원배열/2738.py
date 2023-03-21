# 230321
# 행렬덧셈

# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

n , m = map(int,input().split())
num1 = []
num2 = []
for i in range(n):
    num1.append(list(map(int,input().split())))
for i in range(n):
    num2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        print(num1[i][j]+num2[i][j],end=' ')
    print()

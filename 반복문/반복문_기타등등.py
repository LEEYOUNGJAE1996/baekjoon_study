# 230224
N = int(input())

for i in range(N, 0 , -1):
  for j in range(N):
    if j >= i-1:
      print("*",end="")
    else :
      print(" ",end="")
  print("")

# 230224
result = True
while result:
  a, b = map(int, input().split())
  if a != 0 and b != 0:
    print(a+b)
  else:
    result = False

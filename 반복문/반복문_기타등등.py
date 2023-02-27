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

N = int(input())
a = list(map(int,input().split()))
what = int(input())
count = 0
for i in a:
  if what == i:
    count += 1
print(count)

N = int(input())
ls = list(map(int,input().split()))
max , min = ls[0], ls[0]
for i in ls:
  if i < min:
    min = i
  elif i > max:
    max = i
print(f"{min} {max}")

N , X  = map(int, input().split())
A = list(map(int,input().split()))
for i in A:
  if i < X:
    print(f"{i}",end=" ")

N = int(input())
a = list(map(int,input().split()))
what = int(input())
count = 0
for i in a:
  if what == i:
    count += 1
print(count)

A =[]
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
A.append(int(input()))
max = A[0]
location = 0
for i in A:
  if max < i:
    max = i
    location = A.index(i)
print(max)
print(location+1)


N , M = map(int,input().split())
A=[]
for i in range(N):
  A.append(0)
for i in range(M):
  start,end,number= map(int,input().split(" "))
  for i in range(start,end+1):
    if A[i-1] != number:
      A[i-1] = number
for i in range(N):
  print(A[i],end=" ")

N , M = map(int,input().split())
ls = []
for i in range(1,N+1):
  ls.append(i)
for i in range(M):
  fir , sec = map(int,input().split())
  ls[fir-1],ls[sec-1] = ls[sec-1],ls[fir-1]
print(ls,end=" ")
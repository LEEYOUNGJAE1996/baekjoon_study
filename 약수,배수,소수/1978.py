# 230323
# 소수 찾기
import math
n = int(input())
number = list(map(int,input().split()))
primeNum = 0
for prime in number:
    check = True
    if prime == 1:
        continue
    elif prime < 4 and prime != 1:
        primeNum +=1
    else:    
        for i in range(2,prime):
            if prime % i == 0:
                check = False
                break
        if check == True:
            primeNum +=1
print(primeNum)

# 230323
# 소수 찾기
import math
n = int(input())
number = list(map(int,input().split()))
primeNum = 0
for prime in number:
    check = False
    if prime == 1 :
        continue
    elif prime < 4 and prime != 1 :
        primeNum += 1
    else:
        m = int(math.sqrt(prime))
        for i in range(2,m):
            if m % i == 0 :
                break
        check = True
    if check == True:
        primeNum += 1
print(primeNum)
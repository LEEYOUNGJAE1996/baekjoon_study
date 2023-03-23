# 230323
# 소수

m = int(input())
n = int(input())
primeNum = []
for num in range(m,n+1):
    check = True
    if num == 1:
        continue
    elif num <4:
        primeNum.append(num)
    else:
        for i in range(2,num):
            if num % i == 0:
                check = False
                break
        if check == True:
            primeNum.append(num)
if primeNum == []:
    print(-1)
else:
    print(sum(primeNum))
    print(min(primeNum))

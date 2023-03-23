# 230323
# 약수들의 합

while True:
    num = int(input())
    if num == -1:
        break
    else:
        factors = [factor for factor in range(1,num) if num%factor == 0]
        if num == sum(factors):
            print(f"{num} = ",end='')
            for factor in range(len(factors)-1):
                print(f"{factors[factor]} +",end=' ')
            print(f"{factors[len(factors)-1]}")
        else:
            print(f"{num} is NOT perfect.")
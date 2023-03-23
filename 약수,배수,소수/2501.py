# 230323
# 약수 구하기

n , k = map(int,input().split())

factors = [ num for num in range(1,n+1) if n %num == 0]

if len(factors) < k:
    print(0)
else :
    print(factors[k-1])
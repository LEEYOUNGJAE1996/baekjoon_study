# 230324
# 직사각형에서 탈출

a,b,c,d = map(int,input().split())
list1 = [a,b,abs(a-c),abs(b-d)]
print(min(list1))


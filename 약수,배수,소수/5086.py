# 230323
while True :

    i , j = map(int,input().split())
    if i == 0 and j == 0:
        break
    elif i % j == 0 :
        print('multiple')
    elif j % i == 0:
        print('factor')
    else:
        print('neither')
# 230323
# 소인수분해

# 내가 범한 오류 --- 자기 자신도 출력이 가능하다 소수인 경우
# 만약 다른 수로 나눠진다면 이미 자기 자신이 포함되지 않는다.
# 나눠지는 수가 없을 경우 하나씩 값을 올리는데 이미 그 전에는 원래의 숫자에서 나눌 수 없는 수이다.
# 재귀함수처럼 나누어진 결과에 대해서 계속 소인수분해 함으로
# 최종적으로는 자기 자신을 자신으로 나눠서 몫이 1이 된다.
# 1이 될때까지 구하는 것이 목표였으며, 1이 되면 끝내는 것이 목표였다.


# import time


# num = int(input())
# check = True
# start = 2
# while check:
#     if num != 1:
#         for i in range(start,num+1):
#             check = True
#             if num % i ==0:
#                 print(i)
#                 num = num // i
#                 start = i
#                 break
#             check = False
#         if check == False:
#             print(num)
#     else:
#         break

#다른 사람 코드
num = int(input())
# 시작지점
start = 2
while num > 1:
    if num %start != 0:
        start +=1
    else:
        print(start)
        num = num //start



# 재귀함수 
# start_time = time.time()
# def primeNum(number):
#     if number != 1:
#         for i in range(2,number):
#             if number % i ==0:
#                 print(i)
#                 number = number // i
#                 return primeNum(number)
#         return number
#     else:
#         return number
# number = int(input())
# print(primeNum(number))
# print(-start_time + time.time())

# def primeNum(number):
#     if number != 1:
#         for i in range(2,number):
#             if number % i ==0:
#                 print(i)
#                 number = number // i
#                 return primeNum(number)
#         return number
#     else:
#         return number
# number = int(input())
# print(primeNum(number))
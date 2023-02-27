# 230227
# problem

# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다.
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
# 입력 
#첫째 줄부터 열번 째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
# 이 숫자는 1000보다 작거나 같고, 음이 아닌 정수이다.
# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력

l = []
for i in range(10):
    l.append(int(input()))

remain = []
for i in range(42):
    remain.append(0)

#check 
for i in range(len(l)):
    d = l[i]%42 
    remain[d] += 1 
count = 0
for i in range(len(remain)):
    if remain[i] != 0:
        count +=1

print(count)

# 다른 사람의 풀이
# set함수 집합으로?? {}
# 중복을 허용하지 않는다.
# int(input()) for _ in range(10)
# 10번 반복하면서 for 옆에 int(input()) 을 실행
# print(len(set([int(input()) % 42 for _ in range(10)])))
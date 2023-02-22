# 230222


# 두 수 비교하기
# map을 기억하자 , 리스트 형태의 값을 각 지정해서 타입 변환
# https://www.geeksforgeeks.org/python-map-function/
A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print('<')
else:
    print('==')

# 시험 성적
grade = int(input())
if grade <= 100 and grade >= 90:
    print('A')
elif grade < 90 and grade >= 80:
    print('B')
elif grade < 80 and grade >= 70:
    print('C')
elif grade < 70 and grade >= 60:
    print('D')
else:
    print('F')

# 윤년

year = int(input())
if year % 4 == 0:
    if year % 400 == 0:
        print('1')
    elif year % 100 == 0:
        print('0')
    else:
        print('1')
else:
    print('0')

# 사분면 고르기
# 문제를 정확히 읽고 답을 작성할 것 -> 문제점 그냥 한줄에 작성하고 스플릿으로 문자를 구분함
# 문제에서 제시한 문장  x값을 입력하고 다음 줄에 y값을 입력
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')

# 알람 시계
# 조건을 정확히 파악하자
# 문제의 조건  H 0~ 23 M 0 ~59  이였다 .
# 조건을 너무나 가볍게 무시하고 작성하는 버릇이 있다.
# 종이나 간단히 기억해야할 것을 정리 후 코드로 작성하는 습관을 만들자.
H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = 60 - (45-M)
else:
    M -= 45
print(f"{H} {M}")


# 오븐 시계

# 조건
# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로
# 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다.
# (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)


# 파이썬은 나누기 계산을 하는 경우  float으로 값을 자동 변환이 된다.
# 이점을 유의 해야한다. 정수값을 출력하고 싶은데 모르는 사이에 float 형태의 타입이 반환된다.
H, M = map(int, input().split())
C = int(input())
C_H = C // 60
C_M = C % 60
if C_M + M >= 60:
    M = C_M + M - 60
    H += 1
else:
    M += C_M

if C_H + H >= 24:
    H = (C_H + H) % 24
else:
    H += C_H
print(f"{H} {M}")

# 주사위 상금
# map의 경우 split으로 값을 나눠주는 경우에는 map의 return value는 각 값을 변수에 저장할 수 있다.
# 하지만 리스트를 그대로 반환하고 싶다면 다시 리스트형으로 만들어줘야한다.
# 그렇지 않은 경우 리턴되는 value는 map의 형태로 주소 형태를 가진다
#  예시
# >>> a = map(int, input().split())
# 10 20 (입력)
# >>> a
# <map object at 0x03DFB0D0>
# >>> list(a)
# [10, 20]

a = list(map(int, input().split()))

if a[0] == a[1] and a[0] == a[2]:
    print(10000 + a[0]*1000)
elif a[0] == a[1] or a[0] == a[2]:
    print(1000 + a[0]*100)
elif a[1] == a[2]:
    print(1000 + a[1]*100)
else:
    max = 0
    for num in a:
        if max < num:
            max = num
    print(max * 100)


# 반성할 점 함수를 사용할 때 리턴값이라던가 입력값에 대해서 공부를 하자
# 설계를 할 경우 처음에 신중하게 작성할 것 그 이후 코드로 작성
# 수정하는 일이 생길 경우 정확히 어떤 부분을 어떻게 바꿔야하는지 인식하고
# 바꿔야할 부분을 전부 check  할 것

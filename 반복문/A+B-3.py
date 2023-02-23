# 230223
# 두 정수 A와 B 입력을 받은 다음 A+B로 출력
# 첫줄에 테스트 케이스 개수
# 각 줄에 A와 B 입력

T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f"{A+B}")

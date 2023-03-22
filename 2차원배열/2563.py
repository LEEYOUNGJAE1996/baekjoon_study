# 230322

count = int(input())
# 100 * 100 의 가상의 하얀색 종이를 생성
whitePaper = [[ 0 for i in range(100)] for i in range(100)]
# 검은색 종이의 위치를 입력으로 받는다.
blackPaper = [list(map(int,input().split())) for i in range(count)]
# 검은색 종이에 해당하는 위치에 대해서 1을 저장함으로써 검은색 영역임을 표시
# 겹치는 경우에도 1이 값이 들어가기 떄문에 영향을 미치지 않는다.
for i in range(count):
    for j in range(10):
        for k in range(10):
            whitePaper[j+blackPaper[i][0]-1][k+blackPaper[i][1]-1] = 1
area = 0
for i in range(len(whitePaper)):
    area += sum(whitePaper[i])
print(area)
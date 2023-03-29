# 230329
# 네번째 점 구하기


# 원리 서로 대칭하는 두개의 점을 특정한다. 
# how - 점과 점을 이어 선이라고 했을 경우 3개의 점이므로 
# 직사각형의 경우 2개의 변이 서로 직각하는 점이 생긴다
# 그 점을 제외한 다른 2개의 점이 대칭하는 점으로 존재한다.
# 이를 판단하기 위해서는 2개의 변이 직각함을 판단해야한다.
# 각각의 점을 벡터로 판단하고 

dots = [list(map(int,input().split())) for i in range(3)]

for dot in dots:
    x = []
    y = []
    for compare in dots:
        if dot != compare:
            x.append(dot[0]-compare[0])
            y.append(dot[1]-compare[1])
    if (x[0]*x[1])+(y[0]*y[1]) == 0:
        main = dot
x_sum = 0
y_sum = 0
for i in range(len(dots)):
    if i != dots.index(main):
        x_sum += dots[i][0]
        y_sum += dots[i][1]
center = [x_sum/2,y_sum/2]
final_x = int(center[0]*2-main[0])
final_y = int(center[1]*2-main[1])
print(f'{final_x} {final_y}')
# 230227


N , M = map(int,input().split())
L = []
for i in range(N):
    L.append(i+1)
for i in range(M):
    fir , sec = map(int, input().split())
    L[fir-1] , L[sec-1] = L[sec-1] , L[fir-1]

for i in range(N):
    print(L[i],end=" ")
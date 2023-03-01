# 230302

l = []

n, m = map(int, input().split())
for i in range(1, n+1):
    l.append(i)


for i in range(m):
    fir, sec = map(int, input().split())
    reverse_list = l[fir-1:sec]
    reverse_list.reverse()
    del l[fir-1: sec]
    for i in reverse_list:
        l.insert(fir-1, i)
        fir += 1

for i in range(n):
    print(l[i], end=" ")

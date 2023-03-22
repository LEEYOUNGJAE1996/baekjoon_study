# 230322

num_2d_list = [list(map(int,input().split())) for  i in range(9)]



maxVal = 0
index1 = 0
index2 =0
for i in range(len(num_2d_list)):
    if maxVal < max(num_2d_list[i]):
        maxVal = max(num_2d_list[i])
        index1 = i
        index2 = num_2d_list[i].index(maxVal)
print(maxVal)
print(f'{index1+1} {index2+1}')
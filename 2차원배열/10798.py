# 230322


char_list = [list(input()) for i in range(5)]
new_list = []
input_char = ''
maxLen = 0
for i in range(len(char_list)):
    if maxLen < len(char_list[i]):
        maxLen = len(char_list[i])



for j in range(maxLen):
    for i in range(len(char_list)):
        # print(char_list)
        if char_list[i] != []:
            new_list.append(char_list[i].pop(0))
print(''.join(new_list))


# enumerate 를 활용한 방법
# 1. enumerate
# 인자로 넘어온 목록을 기준으로 인덱스 번호와 배열의 원소를 
# 튜플 형태로 반환
x=['']*75
for i in range(5):
 for j,k in enumerate(input()):x[j*5+i]=k
print("".join(x))
# 230315
# 그룹 단어 체크
# 시간 복잡도 오래걸린다.
# def check(string, index):
#     result = True
#     for letter in range(index, len(string)-1):
#         if string[letter] == string[letter+1]:
#             result = check(string, letter+1)
#         else:
#             if string[:letter+1].find(string[letter+1]) == -1:
#                 resutl = True
#             elif letter+1-string[:letter+1].find(string[letter+1]) > 1:
#                 return False
#     return result


# count = 0
# n = int(input())
# for i in range(n):
#     string = input()
#     if check(string, 0):
#         count += 1
# print(count)


# 그렇다면 어떻게 풀어야할까?
#  굳이 다 체크할 필요가 없다.
n = int(input())
count = 0
for i in range(n):
    string = input()
    repeat = False
    for ind in range(len(string)-1):
        if string[ind] != string[ind+1]:
            if string[:ind+1].find(string[ind+1]) == -1:
                repeat = False
            else:
                repeat = True
                break
    if repeat == False:
        count += 1
print(count)

# 230315

# 단어 공부

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이
# 여러 개 존재하는 경우에는 ?를 출력한다.

# A~Z까지 위치에 대한 값을 받고 count를 통해 각 위치에 따른 글자수가 얼마나 되는지 판단
maximum = []

strings = input().upper()
for i in range(65, 91):
    maximum.append(strings.count("%c" % i))

max_count = 0
counting = 0
index_num = 0
for count in maximum:
    if max_count < count:
        max_count = count

if maximum.count(max(maximum)) > 1:
    print('?')
else:
    print("%c" % (maximum.index(max(maximum))+65))

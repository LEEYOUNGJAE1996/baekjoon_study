# 230310

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
# 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

strings = input().lower()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("함수를 사용하지 않고 문자열을 비교 분석")
for i in range(len(alphabet)):
    find_letter = False
    for j in range(len(strings)):
        if alphabet[i] == strings[j]:
            alphabet[i] = j
            find_letter = True
    if find_letter == False:
        alphabet[i] = -1
    print(alphabet[i], end=" ")

# 함수를 이용하는 방법
# find 함수 --> 해당 문자를 찾은 경우 index값을 보낸다
# 없을 경우 --> -1
# 차이점 index ==> 해당 문자를 찾은 경우 index값을 보낸다.
# 없을 경우 --> Error

print("\nfind 함수를 사용한 결과")
for i in alphabets:
    print(strings.find(i), end=" ")

print("\nindex 함수를 사용한 결과")
for i in alphabetss:
    try:
        print(strings.index(i), end=" ")
    except:
        print("-1", end=" ")

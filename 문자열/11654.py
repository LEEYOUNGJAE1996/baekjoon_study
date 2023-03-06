# 230306

# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때,
# 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.


# 입력으로 주어진 글자의 아스키 코드 값을 출력한다.


#  ord() function
# Given a string representing one Unicode character,
# return an integer representing the Unicode code point of that character.
# For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364.
# This is the inverse of chr().
character = ord(input())
print(character)

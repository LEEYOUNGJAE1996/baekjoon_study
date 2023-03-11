# 230311

# 별찍기
num = int(input())
for count in range(num):
    for i in range(num):
        if i >= num-1-count:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(count):
        if count >= j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for count in range(num-1, 0, -1):
    for i in range(num):
        if i > num-1-count:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(count-1):
        print("*", end="")

    print()


# 다른 사람이 한 방식
n = int(input())
for i in map(abs, range(1-n, n)):
    print(' '*i+'*'*((n-i)*2-1))

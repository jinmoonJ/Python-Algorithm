# 1330 두 수 비교하기
a,b = [int(x) for x in input().split()]
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
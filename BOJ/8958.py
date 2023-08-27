# 8958 OX퀴즈
def solve():
    s = input()
    count = 0
    result = 0
    for c in s:
        if c == "O":
            count += 1
            result += count
        else:
            count = 0
    print(result)

t = int(input())
for _ in range(t):
    solve()

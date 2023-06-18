# SWEA 1865. 동철이의 일 분배
def back(n, a, b):
    global max_p
    if b <= max_p:
        return
    if n == N:
        max_p = max(max_p, b)
        return

    for i in range(N):
        if i not in a:
            a.append(i)
            back(n + 1, a, b * (per[n][i] / 100))
            a.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    per = [list(map(int, input().split())) for _ in range(N)]

    max_p = 0
    back(0, [], 1)
    print(f"#{tc} {max_p * 100:.6f}")

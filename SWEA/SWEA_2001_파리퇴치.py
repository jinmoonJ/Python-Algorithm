# 2001. 파리 퇴치

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    num = 0
    for i in range(n - k + 1):  # 0 1 2 3
        for j in range(n - k + 1):  # 0 1 2 3
            cnt = 0
            for a in range(i, i+k):
                for b in range(j, j+k):
                    cnt += arr[a][b]

                if cnt > num:
                    num = cnt

    print(f"#{tc} {num}")



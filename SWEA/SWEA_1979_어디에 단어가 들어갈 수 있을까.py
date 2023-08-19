# SWEA 1979 어디에 단어가 들어갈 수 있을까
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        cnt = 0
        # 행 검사
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N - 1:
                # 벽을 만났을 때 그동안 쌇아온 cnt 값이 k이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열 검사
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N - 1:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f"#{tc} {ans}")

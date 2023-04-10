# SWEA 12712 파리퇴치3
T = int(input())
for tc in range(1, T + 1):

    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for i in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    ti = [-1, 1, -1, 1]
    tj = [-1, 1, 1, -1]

    total = 0
    answer = 0
    for i in range(n):
        for j in range(n):
            cnt1 = lst[i][j]  # +모양 분사
            cnt2 = lst[i][j]  # x모양 분사
            for k in range(4):  # 방향
                for l in range(1, m):  # 분사 세기
                    a = i + di[k] * l
                    b = j + dj[k] * l

                    c = i + ti[k] * l
                    d = j + tj[k] * l

                    # 인덱스 범위 체크
                    if -1 < a < n and -1 < b < n:
                        cnt1 += lst[a][b]

                    if -1 < c < n and -1 < d < n:
                        cnt2 += lst[c][d]

            total = max(cnt1, cnt2)
            if answer < total:  # 정답 갱신
                answer = total

    print(f"#{tc}", answer)

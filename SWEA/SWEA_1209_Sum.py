# SEWA 1209 sum

T = 10
for tc in range(1, T+1):
    a = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0  # 아주 작은값(계산으로 나올수 있는 값보다 무조건 적게 써야 됨)
    for i in range(N):
        row_sum = 0  # 각 행의 시작시 초기화
        for j in range(N):  # 각행을 돈다
            row_sum += arr[i][j]
        # 이 for 문이 끝나면 arr[i] 행의 합이 row_sum에 저장된 상태
        if max_sum < row_sum:
            max_sum = row_sum

    for i in range(N):  # 열을 먼저 선택
        col_sum = 0
        for j in range(N):  # 행
            col_sum += arr[j][i]
        if max_sum < col_sum:
            max_sum = col_sum

    # 대각 합 구하기
    gak_sum = 0
    for i in range(N):
        gak_sum += arr[i][i]
    if max_sum < gak_sum:
        max_sum = gak_sum

    gak_sum = 0
    for i in range(N):
        gak_sum += arr[i][N - 1 - i]
    if max_sum < gak_sum:
        max_sum = gak_sum

    print(f"#{tc} {max_sum}")
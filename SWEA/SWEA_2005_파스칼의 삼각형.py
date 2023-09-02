# SWEA 2005 파스칼의 삼각형
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(0, i + 1):
            if j == 0 or i == j:  # 열값이 0이거나 행과 열의 값이 같을때
                arr[i][j] = 1
            else:  # 그게 아니라면
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]  # 왼쪽 위와 바로 위의 값의 합을 넣어준다

    print(f"#{tc}")
    for a in range(N):
        for b in range(N):
            if arr[a][b]:
                print(arr[a][b], end=' ')
        print()

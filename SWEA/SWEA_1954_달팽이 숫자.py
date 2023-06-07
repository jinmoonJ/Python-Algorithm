# SWEA 1954. 달팽이 숫자
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    # 우 , 하 , 좌, 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    d = 0  # 현재 채우고 있는 방향
    # di[d] = 0 이면 우로 간다

    snail = [[0] * n for _ in range(n)]  # 0으로 채워진 2차원 배열(크기는 n*n)

    # 맨 첫칸 (0,0) 에 값을 채워놓고 시작
    value = 1
    ci, cj = 0, 0  # 현재(current) 값을 채울 위치 i행 j열

    snail[ci][cj] = value  # 현재 스네일에 값을 채워놓고

    # 반복을 통해 달팽이를 채워나갈껀데
    # 언제까지 채워 나갈까?
    # value가 n*n이 될때까지 계속 반복하면 된다.
    while value < n * n:

        # 일단 다음위치로 한번 가보다
        # 현재 방향은 d에 저장되어 있다.
        ni = ci + di[d]
        nj = cj + dj[d]
        # 가본 다음에 가봤더니 인덱스 범위를 벗어났거나
        # 내가 이미 채웠던 곳이라면 또 방향을 바꿔야 한다.
        # 갈 수 없으면 갈 수 있을때까지 방향을 바꿔보면서 진행
        # 방향은 4번까지밖에 못바꾼다.
        # 상하좌우가 막혀있다. ==> 값채우기가 끝났다. 즉 반복문이 끝남
        for i in range(4):  # i 는 0부터 3 까지
            # d = 0, 1, 2, 3
            d = (d + i) % 4  # 나올수 있는 값의 범위가 4로 나눈 나머지와 같다
            # 다음 방향으로 가보자.
            ni = ci + di[d]
            nj = cj + dj[d]
            # 만약 갈 수 있는 방향이었다. 라면 방향 바꾸기를 종료
            # 인덱스 범위 안인지, 내가 전에 채웠던 위치가 아닌지 검사
            if 0 <= ni < n and 0 <= nj < n and snail[ni][nj] == 0:
                # 갈수 있는 방향을 찾으면 방향 바꾸기를 종료
                ci = ni
                cj = nj
                break

        # 여기까지 오면 갈 수 있는 방향을 찾았다.
        # 값 채우기
        value += 1
        snail[ci][cj] = value

    print(f"#{tc}")
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=" ")
        print()


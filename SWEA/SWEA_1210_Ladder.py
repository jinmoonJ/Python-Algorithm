# SWEA 1210 Ladder 과제

T = 10

for tc in range(1, T + 1):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for col in range(100):  # 도착지점col의 index를 먼저 찾는다
        if ladder[99][col] == 2:
            break

    row = 99  # 도착지점부터 반대로 올라가기 위해서 99시작

    while row > 0:  # 반복은 row가 0이 되면 끝
        if (col - 1 >= 0) and ladder[row][col - 1] == 1:  # 왼쪽 탐색 : col-1 >=0(왼쪽이 0보다 크고) ladder[row][col-1]==1(왼쪽이 1일떄)
            ladder[row][col] = -1
            col -= 1  # 위치를 -1 왼쪽으로
        elif (col + 1 < 100) and ladder[row][col + 1] == 1:  # 오른쪽 탐색
            ladder[row][col] = -1
            col += 1  # 위치를 +1 오른쪽으로
        else:  # 그게 아니면 row를 한칸 위로
            row -= 1

    print(f"#{tc} {col}")

# SWEA 1216 회문2

T = 10

for tc in range(1, T + 1):
    N = int(input())

    lst = [list(input()) for _ in range(100)]
    lst2 = [[lst[i][j] for i in range(100)] for j in range(100)]
    # 입력받은 문자들의 행 열 리스트 100 * 100

    count = 100  # 최대 길이 만들 카운트
    find = False
    while find == False:
        count -= 1
        for a in range(100 - count + 1):
            for b in range(100 - count + 1):
                if lst[a][b:b + count] == lst[a][b:b + count][::-1]:
                    find = True
                if lst2[a][b:b + count] == lst2[a][b:b + count][::-1]:
                    find = True

    print(f"#{tc} {count}")

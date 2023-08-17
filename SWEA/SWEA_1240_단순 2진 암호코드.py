# SWEA 1240 단순 2진 암호코드
num = {'0001101': 0,
       '0011001': 1,
       '0010011': 2,
       '0111101': 3,
       '0100011': 4,
       '0110001': 5,
       '0101111': 6,
       '0111011': 7,
       '0110111': 8,
       '0001011': 9}


def find_end(N, M):
    for i in range(N):
        for j in range(M - 1, 54, -1):
            if arr[i][j] == '1':
                return i, j - 55


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # end = M
    # for i in range(N):
    #     for j in range(M-1, 54, -1):
    #         if arr[i][j]=='1':
    #             end = j
    #             break
    #     if end != M:
    #         break
    si, sj = find_end(N, M)

    code = [0] * 8
    for i in range(8):
        code[i] = num[arr[si][sj:sj + 7]]
        sj += 7

    check = (code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]
    ans = 0
    if check % 10 == 0:
        ans = sum(code)
    print(f'#{tc} {ans}')

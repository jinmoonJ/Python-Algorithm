# SWEA_5789_현주의 상자 바꾸기

T = int(input())
for tc in range(1, T + 1):
    n, q = map(int, input().split())

    lst = [0] * (n + 1)

    for i in range(1, q + 1):
        li, ri = map(int, input().split())
        for j in range(li, ri + 1):
            lst[j] = i

    print(f"#{tc}", end=" ")
    # for ans in lst[1:]:
    #     print(ans, end=" ")
    # print()

    for i in range(1, n+1):
        print(lst[i], end=" ")
    print()

# SWEA 1486 장훈이의 높은 선반

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())

    p = list(map(int, input().split()))

    # p의 부분집합을 모두 구해서
    # 그 원소들의 합이 선반보다 높을 경우 중에 최소값을 구하면 된다.
    answer = 10000 * 21
    for i in range(1 << N):
        min_h = 0
        # j 번째 원소가 포함되어 있는지 확인
        for j in range(N):
            if i & (1 << j):
                min_h += p[j]

        if min_h >= B:
            answer = min(min_h, answer)

    print(f"#{tc} {answer - B}")

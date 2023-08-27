# SWEA 5251 최소 이동 거리

def dijkstra(s, V):  # 시작, 마지막
    U = [0] * (V + 1)
    U[s] = 1  # 시작점

    for i in range(V + 1):
        D[i] = adjM[s][i]

    for _ in range(V + 1):
        u = 0
        minV = INF
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                u = i
                minV = D[i]
        U[u] = 1
        for v in range(V + 1):
            if 0 < adjM[u][v] < INF:
                D[v] = min(D[v], D[u] + adjM[u][v])


T = int(input())
for tc in range(1, T + 1):
    n, e = map(int, input().split())  # N : 마지막 연결지점, E : 도로 개수
    INF = 100
    adjM = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):  # 자기 자신 0
        adjM[i][i] = 0

    for _ in range(e):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0] * (n + 1)
    dijkstra(0, n)

    print(f"#{tc} {D[n]}")

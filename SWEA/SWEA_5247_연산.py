# SWEA 5247 연산

from collections import deque

def bfs(n, m):
    queue = deque()
    queue.append((n, 0))
    check = {}

    while queue:
        item, count = queue.popleft()
        if check.get(item, 0):
            continue
        check[item] = 1
        if item == m:
            return count
        count += 1

        if 0 < item + 1 <= 1000000:
            queue.append((item + 1, count))
        if 0 < item - 1 <= 1000000:
            queue.append((item - 1, count))
        if 0 < item * 2 <= 1000000:
            queue.append((item * 2, count))
        if 0 < item - 10 <= 1000000:
            queue.append((item - 10, count))


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    print(f"#{tc} {bfs(n, m)}")

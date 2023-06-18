# SWEA 1225 암호생성기
from collections import deque

T = 10
for tc in range(1, T + 1):
    N = int(input())
    q = deque(map(int, input().split()))

    cnt = 1
    while q[-1] > 0:  # 큐의 끝이 0이 아니면 반복
        if cnt > 5:  # 1부터 5까지 반복
            cnt = 1
        right = q.popleft() - cnt  # q의 왼쪽 수에서 cnt를 뺴줌
        if right > 0: # 만약 위의 right가 0보다 크면(0이 아니면)
            q.append(right) # q의 오른쪽에 붙여준다
        else:  # 만약 0이거나 0보다 작으면
            q.append(0) # q에 숫자 0을 넣어준다
        cnt += 1 # 1 ~ 5까지 반복해야 하기 때문에 cnt를 1 올려준다

    print(f'#{tc}', end=" ")
    for i in q:
        print(i, end=" ")
    print()

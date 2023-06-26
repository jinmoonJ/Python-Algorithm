# 1번 풀이
def solution(arr, queries):
    answer = []

    a = 0  # 시작 인덱스
    b = 0  # 반복 횟수
    maxV = 0  # 비교할 값

    for x in range(len(queries)):  # 0 1 2
        a = queries[x][0]  # 시작 인덱스 값
        b = queries[x][1]  # 반복횟수 구하기 4 3 2
        maxV = queries[x][-1]  # 비굣값 2 2 2
        mlist = [1000001] # 문제의 조건 중 가장 큰 수가 1000000 -> 비교 값으로 더 큰 값을 넣어놓음

        for i in range(a, b + 1):  # 4번방까지 반복
            if arr[i] > maxV:
                mlist.append(arr[i])

        if min(mlist) == 1000001: # 비교했을 때 초기의 1000001 값만 있다는 건 비굣값보다 큰 값이 없다 -> -1 출력
            answer.append(-1)
        else: # 그게 아니면 비굣값 보다 큰 값이 있는 것 그 중에 가장 작은 값을 answer에 저장해 출력
            answer.append(min(mlist))

    return answer
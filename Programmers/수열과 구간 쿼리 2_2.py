def solution(arr, queries):
    answer = []

    a = 0  # 시작 인덱스
    b = 0  # 반복 횟수
    maxV = 0  # 비교할 값

    for x in range(len(queries)):  # 0 1 2
        a = queries[x][0]  # 시작 인덱스 ㄱ밧
        b = queries[x][1]  # 반복횟수 구하기 4 3 2
        maxV = queries[x][-1]  # 비굣값 2 2 2
        mlist = []

        for i in range(a, b + 1):  # 4번방까지 반복
            if arr[i] > maxV:
                mlist.append(arr[i])
        # 실행할 코드
        try: # mlist의 최소값이 비굣값보다 크면 answer에 저장
            if min(mlist) > maxV:
                answer.append(min(mlist))
        # 예외 발생했을 때 실행할 코드
        except: # mlist의 최소값이 같으면 -1 출력
            answer.append(-1)

    return answer
# SWEA 1208 Flatten

T = 10
for t in range(1, T + 1):
    N = int(input())
    list1 = list(map(int, input().split()))

    # 입력 받은 리스트를 정렬을 시킨 다음
    # 최대 값(list1[-1]) 과 최소 값(list1[0])에 덤프 횟수(N) 만큼 반복해서
    # 1을 빼고 더해줘서 평탄화 시키고 정렬 과정을 반복
    # 평탄화를 N번 만큼 진행하고 남은 list1의 max값에 min 값을 빼면 높이 차가 나오는데
    # answer값이 높이의 차보다 클 경우에만 넣어준다

    answer = 100  # max_box와 min_box를 더해도 100 이하이기 때문에 초기 값으로 100 설정
    for i in range(N):
        list1.sort()
        # print(list1)
        list1[0] += 1
        list1[-1] -= 1
        if answer > max(list1) - min(list1):
            answer = max(list1) - min(list1)
        # print(answer)

    print(f"#{t} {answer}")
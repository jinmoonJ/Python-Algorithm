# SWEA 1206 View

T = 10  # 10의 테스트 케이스가 주어졌음 int(input())
for t in range(1, T + 1):
    n = int(input())
    list1 = list(map(int, input().split()))

    answer = 0  # 조망권 획득 방 개수 합을 저장할 변수

    for i in range(2, n - 2):  # 제약사항의 처음과 끝의 2칸은 건물이 X기 때문에 2번부터 n-2까지만 구한다
        high = list1[0]  # for문을 순회하는 동안 가장 높은 방의 기준(초기값) => 처음은 0칸인 list의 0번방
        for j in range(i - 2, i + 3):  # 앞 뒤로 2칸을 비교해야 하기 때문에 i-2부터 i+3까지 순회
            if j == i:  # i의 값과 j의 값이 같으면 넘어가고
                continue
            elif high < list1[j]:  # high와 비교한 list1[j]의 값이 크면
                high = list1[j]  # list1[j]값을 high에 할당한다
        # 이 for 문이 끝나면 앞 뒤로 두칸 중 가장 높은 층수(high)가 구해진다

        # 앞 for 문에서 구한 주변의 가장 높은 층수(high)를 list[i]에서 빼면 조망권이 확보된 층의 갯수
        if list1[i] > high:  # list[i]의 값이 high보다 크면
            answer += list1[i] - high  # 확보된 층의 갯수를 answer에 누적
    print(f"#{t} {answer}")
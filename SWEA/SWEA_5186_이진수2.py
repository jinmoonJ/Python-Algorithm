# SWEA 5186 이진수2

# 바꿔주는 함수
def change(n):
    # 몇번 바꿨는지 세줄 변수 초기화
    cnt = 0
    # 결과값 초기화
    result = ''
    # 2진법 자리수 시작
    a = 1
    # n이 0이 될때까지 돌린다.
    while n:
        # 만약 n보다 2진법 자리가 크다면 0을 붙인다.
        if n < 2 ** -a:
            result += '0'
        # 아니라면 1을 붙인다.
        else:
            n -= 2 ** -a
            result += '1'
        # 붙이고 나서 횟수를 더해준다.
        cnt += 1
        # 만약 12회가 넘어간다면 오버플로우로 끝낸다.
        if cnt > 12:
            return 'overflow'
        # 아니라면 다음 자리수를 봐보자
        else:
            a += 1
    # 12자리까지 딱 나누어 떨어졌으면 결과값을 반환하자
    return result


T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    print(f"#{tc} {change(N)}")

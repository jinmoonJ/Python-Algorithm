# SWEA 5432 쇠막대기 자르기
T = int(input())
for tc in range(1, T + 1):
    lst = list(input()) # 리스트로 받아서
    stick = 0
    cnt = 0
    l = len(lst)
    i = 0
    while i < l:
        if lst[i] == '(' and lst[i + 1] == ')':  # ( 다음 ) 나오면 레이저
            cnt += stick
            i += 2
        elif lst[i] == '(':  # ) 오지 않으면 쇠막대 => 쇠막대기 개수 1 증가
            stick += 1
            i += 1
        else:  # 나머지 ) 는 쇠막대 끝
            cnt += 1
            stick -= 1
            i += 1
    print(f"#{tc} {cnt}")

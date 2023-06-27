# 2439 별 찍기 - 2
n = int(input()) # 5를 입력했다고 가정 하고 풀이
for i in range(1, n+1): # 1부터 6까지 즉, 1,2,3,4,5
    for _ in range(n-i): # 5-i 행번호만큼
        print(" ", end='') # 공백 추가하고 개행 없이
    for _ in range(i):
        print("*", end='') # *을 출력
    print("")
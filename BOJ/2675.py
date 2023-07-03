# 2675 문자열 반복
def solve():
    R, S = input().split() # 반복횟수 R, 문자열 S
    R = int(R) # 반복횟수인 R은 숫자 int로 변환
    for a in S: # 문자열을 돌면서
        print(a*R, end='') # 각 문자열을 반복횟수 R번 반복출력
    print("") # 반복문 끝나면 줄 바꿈 후 다음 문제 수행

t = int(input()) # 1. tc 개수 입력
for _ in range(t):
    solve() # 2. solve() 함수를 tc 개수만큼 실행
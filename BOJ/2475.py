# 2475 검증수
arr = [int(x) for x in input().split()]
sumA = 0 # 입력받은 고유번호의 총 합계
for item in arr:
    sumA += (item * item) # 각 고유번호의 제곱값을 저장
print(sumA%10) # 저장한 총 합계에 10을 나눈 나머지 값 출력
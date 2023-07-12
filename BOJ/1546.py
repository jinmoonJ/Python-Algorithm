# 1546 평균
n = int(input()) # 과목 수
arr = [int(x) for x in input().split()] # 과목 별 점수 int 값으로 받기
maxV = max(arr) # arr의 가장 큰 값을 찾기
sumA = 0 # 새로 만든 점수 저장 (총점수)
for item in arr: # 입력받은 과목 점수를 돌면서
    sumA += ((item/maxV) * 100) # 새로운 점수 생성해서 저장
print(sumA/n) # 새로 만든 총점 / 과목 수 ==> 새로운 평균값 출력

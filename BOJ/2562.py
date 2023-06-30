# 2562 최댓값
n = 9 # 주어진 자연수의 수
arr = [] # 입력받은 자연수를 저장할 빈 리스트 생성
for _ in range(n): # 주어진 자연수의 수 만큼 반복해서
    arr.append(int(input())) # 입력받은 자연수를 arr리스트에 추가
maxV = 0 # 가장 큰 값 저장
for i in range(n):
    if maxV < arr[i]: # maxV값보다 리스트의 값이 클 경우
        idx = i # index 값을 저장(0~8)
        maxV = arr[i] # arr의 i번째의 값을 maxV에 저장
print(maxV) # 저장한 maxV의 값 출력
print(idx+1) # index는 0부터 시작하기 때문에 +1 해서 index 출력
# 1157 단어공부
s = input()
s = s.upper()
dict1 = {} # 딕셔너리로 key(단어)와 value(횟수)를 저장
for c in s:
    if c in dict1.keys(): # 나온 단어가 딕트에 있으면
        dict1[c] += 1 # 같은 단어가 있으면 1 증가
    else:
        dict1[c] = 1 # 없는데 처음 나온거면 기본 값 1을 준다.

maxV = 0 # 가장 많이 나온 단어 횟수

for i in dict1.keys(): # 딕셔너리의 키값을 통해 순회
    maxV = max(maxV, dict1[i]) # maxV와 dict1[키(단어)] 중 큰 수를 maxV에 저장
cnt = 0 # 횟수가 같은지 아닌지 확인하기 위한 카운트
for i in dict1.keys(): # 딕셔너리를 순회
    if dict1[i] == maxV: # 딕셔너리의 key의 value가 maxV와 같으면
        cnt += 1 # 카운트를 +1 (횟수가 같은 value있으면 1이 아니게됨)
        result = i # 가장 많이 나온 횟수의 key(단어)를 저장
if cnt != 1: # maxV가 같은 단어가 두개 이상이면 1이 아니게 됨
    print("?") # ? 출력
else: # 1개의 단어만 횟수가 많으면
    print(result) # 저장한 result 값 출력




# 2577 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

T = a * b * c
list1 = [0] * 10 # 0부터 9까지 횟수 구해야 하기 때문에 10개

while T != 0: # T의 값이 0이 될때까지 반복 수행
    # T값을 10으로 나눈 나머지에 맞는 인덱스의 값에 1을 추가
    # ex) 17037이면 10으로 나눈 나머지(7), list1[7]에 1추가
    list1[T % 10] += 1
    T //= 10 # T를 10으로 나눈 후 몫을 새롭게 T로 할당

for i in list1: # list1를 돌면서 전체 출력
    print(i)
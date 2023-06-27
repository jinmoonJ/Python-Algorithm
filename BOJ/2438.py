# 2438 별 찍기 - 1
n = int(input())
for i in range(n): # 행은 n개 생성하고,
    for j in range(i+1): # 0부터 시작하기 때문에 i+1, 행의 수에 맞게 1 ~ n개 까지
        print("*", end='') # end를 사용해서 개행없이(다음 출력물과 붙여서 출력)
    print("")
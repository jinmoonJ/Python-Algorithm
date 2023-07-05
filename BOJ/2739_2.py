# 2739 구구단
N = int(input())
# 하나씩 개행 하지 않고 출력
for i in range(1,10):
    print(N, end='')
    print(" * ", end='')
    print(i, end='')
    print(" = ", end='')
    print(N*i)
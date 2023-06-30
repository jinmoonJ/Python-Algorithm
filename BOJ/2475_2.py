# 2475 검증수 풀이 2
arr = [int(x) for x in input().split()]

sumA = 0
for i in arr:
    z = i*i
    sumA += z
print(sumA%10)
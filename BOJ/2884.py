# 2884 알람 시계
H, M = [int(x) for x in input().split()]
T = ((H * 60 + M - 45) + (24*60)) % (24*60)
M = T % 60
H = T // 60
print(H,M)

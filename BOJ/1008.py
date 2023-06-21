# 1001 A/B
# input으로 입력받은 값은 문자열로 들어오기 때문에
# int(x)로 int형으로 형변환
a, b = [int(x) for x in input().split()]
print(a/b)

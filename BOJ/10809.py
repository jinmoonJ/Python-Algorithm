# 10809 알파벳 찾기
def idx(c):
    return ord(c) - ord('a')

s = input()
SZ = idx('z') + 1
rst = [-1]*SZ
for i in range(len(s)):
    if rst[idx(s[i])] == -1:
        rst[idx(s[i])] = i
for item in rst:
    print(item, end=' ')
print("")
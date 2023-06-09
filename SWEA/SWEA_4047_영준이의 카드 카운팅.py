# SWEA 4047. 영준이의 카드 카운팅

dct = {"S": 0, "D": 1, "H": 2, "C": 3}

T = int(input())
for tc in range(1, T + 1):
    st = input()
    arr = [[] for _ in range(4)]

    # 리스트에 추가
    for i in range(0, len(st), 3):
        arr[dct[st[i]]].append(int(st[i + 1:i + 3]))

    ans = []
    for lst in arr:
        if len(lst) != len(set(lst)):  # 오류
            print(f"#{tc} ERROR")
            break
        ans.append(13 - len(lst))
    else:
        print(f"#{tc}", end=" ")
        for i in ans:
            print(i, end=" ")
        print()

        # print(f"#{tc}", *ans)

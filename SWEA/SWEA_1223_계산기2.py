# SWEA 1223 계산기2
T = 10
for tc in range(1, T + 1):
    N = int(input())
    infix = input()
    S = []  # push : list.append(), pop : list.pop()
    postfix = ""

    for token in infix:
        if token == "+" or token == "*":  # if token in "+*"
            # token 과 S[top](스택의꼭대기 = 리스트의 마지막)과 우선순위 비교
            while S and token == "+" and S[-1] == "*":  # S and => 스택이 비었는지 확인
                postfix += S.pop()
            # while S and token == S[-1]:
            #     prefix += S.pop()
            S.append(token)
        else:
            postfix += token

    while S:
        postfix += S.pop()

    # 후위 표기 계산하기
    for token in postfix:
        if token in "+*":
            b = S.pop()
            a = S.pop()
            if token == "+":
                S.append(a + b)
            else:
                S.append(a * b)
        else:
            S.append(int(token))

    print(f"#{tc} {S[0]}")

# SWEA_1224 계산기3
T = 10
icp = {"+": 1, "*": 2, "(": 3, ")": 0}  # 스택안에서의 우선순위
isp = {"+": 1, "*": 2, "(": 0, ")": 0}  # 스택안에서의 우선순위
for tc in range(1, T + 1):
    N = int(input())
    infix = input()
    S = []  # push : list.append(), pop : list.pop()
    postfix = ""

    for token in infix:
        if token in icp:  # if token in "+*"
            # token 과 S[top](스택의꼭대기 = 리스트의 마지막)과 우선순위 비교
            if token == ")":
                while S and S[-1] != "(":
                    postfix += S.pop()
                S.pop()
            else:
                while S and icp[token] <= isp[S[-1]]:  # S and => 스택이 비었는지 확인
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

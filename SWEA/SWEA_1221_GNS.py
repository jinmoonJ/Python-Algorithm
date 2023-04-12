# SWEA 1221 GNS
T = int(input())
for tc in range(1, T + 1):
    N = input()
    str_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    # 개수 저장 하는 딕셔너리 생성
    str_list = input().split()
    result = "" # 빈 문자열 생성
    for s in str_list:  # 각각 갯수 누적
        str_dict[s] += 1

    for key, value in str_dict.items():  # 각 원소가 몇개인지 나오기때문에 앞에서부터 개수만큼 생성한다.
        temp = ' '.join([key] * value)  # temp에 value개수만큼의 key를 넣고
        result += temp + ' '  # result에 temp와 공백을 넣어준다

    print(f"#{tc}")
    print(result[:len(result)])  # result 길이만큼

# SWEA 1966 숫자를 정렬하자 (bubble)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = list(map(int, input().split()))

    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    result = " ".join(map(str, numbers))
    print(f"#{tc} {result}")

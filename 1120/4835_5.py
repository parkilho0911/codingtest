# 4835. [S/W 문제해결 기본] 1일차 - 구간합 D2

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    total = []
    for i in range(n-m+1):
        score = 0
        for j in range(m):
            score += a[i+j]
        total.append(score)

    total.sort()

    min_array = total[0]
    max_array = total[-1]
    answer = max_array - min_array
    print(f"#{test_case} {answer}")
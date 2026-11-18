# 4835. [S/W 문제해결 기본] 1일차 - 구간합 D2
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    total = []

    for i in range(n-m+1):
        sum_a = 0

        for j in range(m):
            sum_a += a[i+j]
        total.append(sum_a)

    total.sort()
    min_total = total[0]
    max_total = total[-1]
    answer = max_total - min_total
    print(f"#{test_case} {answer}")
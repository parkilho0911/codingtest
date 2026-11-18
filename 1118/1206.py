# 1206. [S/W 문제해결 기본] 1일차 - View D3
t = 10

for test_case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    total = 0

    for i in range(2, n-2):
        nearby = [a[i-2], a[i-1],a[i+1], a[i+2]]
        if a[i] > max(nearby):
            total += a[i] - max(nearby)

    print(f"#{test_case} {total}")
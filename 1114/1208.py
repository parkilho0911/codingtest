# 1208. [S/W 문제해결 기본] 1일차 - Flatten D3
t = 10

for test_case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        max_a = max(a)
        min_a = min(a)

        if max_a - min_a <= 1:
            break

        max_index = a.index(max_a)
        min_index = a.index(min_a)

        a[max_index] -= 1
        a[min_index] += 1

    max_a = max(a)
    min_a = min(a)

    answer = max_a - min_a
    print(f"#{test_case} {answer}")

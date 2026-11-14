# 20728. 공평한 분배 2 D3
t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    total = []
    for i in range(n-k+1):
        diff = a[i+k-1] - a[i]
        total.append(diff)

    answer = min(total)
    print(f"#{test_case} {answer}")
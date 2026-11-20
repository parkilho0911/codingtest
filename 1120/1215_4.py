# 1215. [S/W 문제해결 기본] 3일차 - 회문1 D3
t = 10

for test_case in range(1, t+1):
    n = int(input())

    a = []
    for i in range(8):
        a.append(list(input().strip()))

    total = []
    count = 0

    for j in range(8):
        for k in range(8-n+1):
            total = a[j][k:k+n]
            if total == total[::-1]:
                count += 1

            total = []
            for offset in range(n):
                total.append(a[k + offset][j])

            if total == total[::-1]:
                count += 1

    print(f"#{test_case} {count}")
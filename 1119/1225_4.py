# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 D3
t = 10

for test_case in range(1, t+1):
    test_number = int(input())

    a = list(map(int, input().split()))

    total = 0

    i = 0
    while a[7] > 0:
        if a[7] <= 0:
            break

        for j in range(1, 6):
            total = a[0] - j
            a.pop(0)

            if total <= 0:
                a.append(0)
                break
            else:
                a.append(total)

    print(f"#{test_case}", *a)
# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 D3
t = 10

for test_case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    j = 1

    while True:
        first = a.pop(0)
        first -= j

        if first <= 0:
            a.append(0)
            break

        a.append(first)

        j += 1
        if j == 6:
            j = 1

    print(f"#{test_case}", *a)
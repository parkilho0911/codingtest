# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 D3
t = 10

for test_case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    b = 0

    while a[7] > 0:
        for i in range(1, 6):
            b = a[0] - i
            a.pop(0)

            if b <= 0:
                a.append(0)
                break
            a.append(b)



    print(f"#{test_case}", *a)
# 1220. [S/W 문제해결 기본] 5일차 - Magnetic D3
t = 10

for test_case in range(1, t+1):
    n = int(input())

    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    # 1이 내려가는거 2가 올라가는거
    count = 0

    for i in range(n):
        has_one = False
        for j in range(n):
            if a[j][i] == 1:
                has_one = True
            elif a[j][i] == 2 and has_one == True:
                count += 1

                has_one = False


    print(f"#{test_case} {count}")


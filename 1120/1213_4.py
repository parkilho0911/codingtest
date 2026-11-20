# 1213. [S/W 문제해결 기본] 3일차 - String D3
t = 10

for test_case in range(1, t+1):
    n = int(input())
    s = input()

    a = list(map(str, input().strip()))
    count = 0

    for i in range(len(a) - len(s) + 1):
        if s == "".join(a[i:i+len(s)]):
            count += 1

    print(f"#{test_case} {count}")
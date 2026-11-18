# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호 D3
t = 10

for test_case in range(1, t+1):
    n, m = map(str, input().split())

    a = []
    for i in m:
        a.append(int(i))

    i = 0
    while i < len(a) - 1:
        if a[i] == a[i+1]:
            a.pop(i)
            a.pop(i)
            i -= 1

            if i < 0:
                i = 0
        else:
            i += 1
    total = ""
    for k in a:
        total += str(k)
    print(f"#{test_case} {total}")
# 5356. 의석이의 세로로 말해요 D3
t = int(input())

for test_case in range(1, t+1):
    a = []
    for i in range(5):
        a.append(list(input().strip()))
    max_a = max(map(len, a))

    total = ""

    for j in range(max_a):
        for k in range(5):
            if j >= len(a[k]):
                pass
            else:
                total += a[k][j]

    print(f"#{test_case} {total}")
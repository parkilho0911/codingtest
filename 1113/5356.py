# 5356. 의석이의 세로로 말해요 D3
t = int(input())

for test_case in range(1, t+1):
    a = []
    for i in range(5):
        a.append(list(map(str, input().strip())))

    total = ""
    max_length = max(map(len, a))
    for j in range(max_length):
        for k in range(5):
            if j >= len(a[k]):
                continue
            total += a[k][j]
    print(f"#{test_case} {total}")

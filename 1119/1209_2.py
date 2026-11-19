# 1209. [S/W 문제해결 기본] 2일차 - Sum D3
t = 10

for test_case in range(1, t+1):
    case_number = int(input())
    n = 100

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    score = []

    for row in range(n):
        row_total = 0
        col_total = 0
        for col in range(n):
            row_total += a[row][col]
            col_total += a[col][row]
        score.append(row_total)
        score.append(col_total)

    left_cross = 0
    right_cross = 0

    for j in range(n):
        left_cross += a[j][j]
        right_cross += a[n-1-j][j]
    score.append(left_cross)
    score.append(right_cross)
    answer = max(score)

    print(f"#{test_case} {answer}")
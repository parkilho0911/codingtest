# 15612. 체스판 위의 룩 배치 D3
# 과정 : n = 8 이렇게 선정을 한다.
t = int(input())

for test_case in range(1, t+1):
    n = 8
    row_count = [0] * 8
    col_count = [0] * 8
    a = []
    for i in range(n):
        a.append(list(map(str, input())))

    for row in range(n):
        for col in range(n):
            if a[row][col] == "O":
                row_count[row] += 1

            if a[col][row] == "O":
                col_count[row] += 1

    answer = "yes"

    for j in row_count:
        if j != 1:
            answer = "no"

    for k in col_count:
        if k != 1:
            answer = "no"

    print(f"#{test_case} {answer}")
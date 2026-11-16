# 11315. 오목 판정 D3
t = int(input())
# 가로 세로 우대각 왼대각
dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]

for test_case in range(1, t+1):
    n = int(input())
    a = []
    answer = "NO"
    for i in range(n):
        a.append(list(input().strip()))

    for y in range(n):
        for x in range(n):
            if a[y][x] == "o":

                for j in range(4):
                    count = 0
                    for k in range(5):
                        nx = x + dx[j] * k
                        ny = y + dy[j] * k

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue

                        if a[ny][nx] != "o":
                            break

                        count += 1
                    if count == 5:
                        answer = "YES"

    print(f"#{test_case} {answer}")
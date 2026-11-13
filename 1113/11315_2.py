# 11315. 오목 판정 D3 복습
t = int(input())
# 오른쪽, 아래, 오른쪽 대각, 왼쪽 대각
dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

for test_case in range(1, t+1):
    n = int(input())

    a = []
    for i in range(n):
        a.append(list(input()))

    answer = "NO"

    for row in range(n):
        for col in range(n):

            for j in range(4):
                count = 0

                for k in range(5):
                    nx = col + dx[j] * k
                    ny = row + dy[j] * k

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if a[ny][nx] != "o":
                        break
                    count += 1

                if count == 5:
                    answer = "YES"
                    break
    print(f"#{test_case} {answer}")
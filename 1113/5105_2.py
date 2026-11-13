# 5105. [S/W 문제해결 기본] 6일차 - 미로의 거리 D3 복습
from collections import deque
t = int(input())
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, t+1):
    n = int(input())

    a = []
    for i in range(n):
        a.append(list(map(int, input())))

    for j in range(n):
        for k in range(n):
            if a[j][k] == 2:
                x = k
                y = j

    b = []
    for h in range(n):
        b.append([-1] * n)

    def bfs(x, y):
        b[y][x] = 0

        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()

            if a[y][x] == 3:
                return b[y][x] - 1

            for g in range(4):
                nx = x + dx[g]
                ny = y + dy[g]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if a[ny][nx] != 1 and b[ny][nx] == -1:
                    b[ny][nx] = b[y][x] + 1

                    queue.append((nx, ny))
        return 0
    answer = bfs(x, y)
    print(f"#{test_case} {answer}")

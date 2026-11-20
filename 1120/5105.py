# 5105. [S/W 문제해결 기본] 6일차 - 미로의 거리 D3
from collections import deque
t = int(input())
# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, t+1):
    n = int(input())
    a = []
    for i in range(n):
        a.append((list(map(int, input().strip()))))

    for row in range(n):
        for col in range(n):
            if a[col][row] == 2:
                x = row
                y = col

    visited = []
    for j in range(n):
        visited.append([-1] * n)

    def bfs(x, y):
        visited[y][x] = 0

        queue = deque([(x,y)])
        while queue:
            x, y = queue.popleft()

            if a[y][x] == 3:
                return visited[y][x] - 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if a[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx, ny))

                if a[y][x] == 3:
                    break
        return 0


    answer = bfs(x,y)
    print(f"#{test_case} {answer}")
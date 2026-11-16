# 5105. [S/W 문제해결 기본] 6일차 - 미로의 거리 D3
from collections import deque
t = int(input())
# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, t+1):
    N = int(input())
    a = []
    for i in range(N):
        a.append(list(map(int, input())))

    for j in range(N):
        for k in range(N):
            if a[j][k] == 2:
                x = k
                y = j

    visited = []
    for h in range(N):
        visited.append([-1]*N)


    def bfs(x,y):
        visited[y][x] = 0

        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()

            if a[y][x] == 3:
                return visited[y][x] - 1

            for g in range(4):
                nx = x + dx[g]
                ny = y + dy[g]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if a[y][x] == 1 or visited[ny][nx] != -1:
                    continue

                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx,ny))
        return 0
    answer = bfs(x, y)
    print(f"#{test_case} {answer}")


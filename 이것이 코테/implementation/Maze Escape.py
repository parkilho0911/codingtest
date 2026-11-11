#미로 탈출
#괴물이 있는 부분이 0, 없는 부분이 1
# 먼저 넣은 좌표부터 꺼내기 위해 deque를 사용합니다.
from collections import deque
n,m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))
#이동할 네 가지 방향 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x, y):
    distance = []
    for i in range(n):
        distance.append([0]*m)
    # 앞으로 주변을 확인할 좌표들을 저장합니다.
    queue = deque()

    distance[x][y] = 1
    queue.append((x, y))

    # 확인할 좌표가 남아 있는 동안 반복합니다.
    while queue:
        # 가장 먼저 넣은 좌표를 꺼냅니다.
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if distance[nx][ny] != 0:
                continue

            distance[nx][ny] = distance[x][y]+1

            queue.append((nx, ny))


    return distance[n-1][m-1]

print(bfs(0,0))
# 5105. [S/W 문제해결 기본] 6일차 - 미로의 거리 D3
from collections import deque
t = int(input())

# 상 하 좌 우에 대한 값을 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, t+1):
    n = int(input())

    a = []
    for i in range(n):
        a.append(list(map(int, input())))

    # 출발 위치 찾는 것
    for j in range(n):
        for k in range(n):
            if a[j][k] == 2:
                x = j
                y = k

    distance = []
    for h in range(n):
        distance.append([-1]*n)

    # 함수안에서 내가 만들어야 할 것
    # 2에서 출발해야 4개의 방향 중에 0 인것을 찾아서 그 좌표를 stack에 저장을 해야해

    def bfs(x, y):
        distance[x][y] = 0
        queue = deque([(x, y)]) # 출발점을 첫 번쨰 탐색 대상으로 지정하는 것이다.

        while queue:
            x, y = queue.popleft() # 가장 먼저 들어온 좌표를 꺼낸다

            for g in range(4):
                nx = x + dx[g]
                ny = y + dy[g]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if a[nx][ny] != 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1 # 그 칸을 처음 발견했을 때 이동 거리를 기록합니다.

                    queue.append((nx, ny))

                if a[x][y] == 3:
                    return distance[x][y] - 1
        return 0
    answer = bfs(x, y)
    print(f"#{test_case} {answer}")

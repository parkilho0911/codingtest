# 4875. [S/W 문제해결 기본] 5일차 - 미로 D2
# 4875번 미로
t = int(input())

# 상·하·좌·우의 행과 열 변화량입니다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, t + 1):
    # n×n 미로를 입력받습니다.
    n = int(input())
    a = []

    for i in range(n):
        a.append(list(map(int, input().strip())))

    # 출발점 2의 행과 열을 찾습니다.
    for j in range(n):
        for k in range(n):
            if a[j][k] == 2:
                x = j
                y = k

    # 각 칸의 방문 여부를 저장할 2차원 리스트입니다.
    visited = []
    for i in range(n):
        visited.append([False] * n)

    # 출발 위치에서 목적지까지 갈 수 있는지 탐색합니다.
    def dfs(x, y):
        # 앞으로 주변을 확인할 좌표를 스택에 저장합니다.
        stack = [(x, y)]

        # 출발점은 스택에 넣었으므로 방문 표시합니다.
        visited[x][y] = True

        # 확인할 좌표가 남아 있는 동안 반복합니다.
        while stack:
            # 마지막에 넣은 좌표를 꺼냅니다.
            x, y = stack.pop()

            # 꺼낸 칸이 목적지라면 성공을 반환합니다.
            if a[x][y] == 3:
                return 1

            # 현재 위치의 상하좌우를 확인합니다.
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위 밖이면 이번 방향은 건너뜁니다.
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                # 벽이거나 이미 방문 표시한 칸이면 건너뜁니다.
                if a[nx][ny] == 1 or visited[nx][ny] == True:
                    continue

                # 새로운 칸은 방문 표시하고 스택에 넣습니다.
                visited[nx][ny] = True
                stack.append((nx, ny))

        # 갈 수 있는 곳을 모두 확인했는데 목적지를 못 찾았습니다.
        return 0

    # 찾은 출발 좌표로 탐색을 시작합니다.
    answer = dfs(x, y)

    # 도착 가능하면 1, 불가능하면 0을 출력합니다.
    print(f"#{test_case} {answer}")
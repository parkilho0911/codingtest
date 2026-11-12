# 4875. [S/W 문제해결 기본] 5일차 - 미로 D2
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for test_case in range(1, t+1):
    n = int(input())
    a = [] # 미로를 담을 수 있는 빈 리스트
    for i in range(n): # 미로를 담기
        a.append(list(map(int, input())))

    # 출발점인 2를 찾는다
    for j in range(n):
        for k in range(n):
            if a[j][k] == 2:
                x = j
                y = k

    visited = [] # 방문을 확인하는 리스트
    for l in range(n):
        visited.append([False]*n)

    def dfs(x, y):
        visited[x][y] = True # 방문 처리 배열 필수 처리 조건

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            if a[nx][ny] == 3: # 재귀 함수 종료 조건
                return 1

            for m in range(4):
                nx = x + dx[m]
                ny = y + dy[m]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if a[nx][ny] != 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True

                    stack.append([nx, ny])


        return 0
    answer = dfs(x, y)

    print(f"#{test_case} {answer}")
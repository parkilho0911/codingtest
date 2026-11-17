# 4615. 재미있는 오셀로 게임 D3
t = int(input())

# 좌, 우, 상, 하, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    # 0으로 채운 n×n 게임판을 만든다.
    game = []
    for i in range(n):
        game.append([0] * n)

    # 가운데 네 칸에 초기 돌을 놓는다. 1은 흑돌, 2는 백돌이다.
    mid = n // 2
    game[mid - 1][mid - 1] = 2
    game[mid - 1][mid] = 1
    game[mid][mid - 1] = 1
    game[mid][mid] = 2

    # 입력받은 순서대로 m번 돌을 놓는다.
    for j in range(m):
        x, y, s = map(int, input().split())

        # 문제 좌표를 0부터 시작하는 리스트 인덱스로 바꾼다.
        x -= 1
        y -= 1

        # 해당 위치에 이번 색의 돌을 놓는다.
        game[y][x] = s

        # 놓은 돌을 기준으로 8방향을 각각 확인한다.
        for k in range(8):
            # 이번 방향에서 뒤집을 후보 좌표를 저장한다.
            flip = []

            # 출발점에서 1칸, 2칸, 3칸… 떨어진 곳을 확인한다.
            for step in range(1, n):
                nx = x + dx[k] * step
                ny = y + dy[k] * step

                # 판 밖이면 이번 방향의 검사를 끝낸다.
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break

                # 빈칸이면 양 끝이 내 돌로 연결되지 않는다.
                if game[ny][nx] == 0:
                    break

                # 내 돌을 만나면 사이에 모아둔 상대 돌을 뒤집는다.
                if game[ny][nx] == s:
                    for fx, fy in flip:
                        game[fy][fx] = s
                    break

                # 상대 돌이면 뒤집을 후보로 위치를 저장한다.
                flip.append((nx, ny))

    # 모든 수를 진행한 뒤 흑돌과 백돌의 개수를 센다.
    black = 0
    white = 0

    for row in game:
        for stone in row:
            if stone == 1:
                black += 1
            elif stone == 2:
                white += 1

    # 흑돌 개수, 백돌 개수 순서로 출력한다.
    print(f"#{test_case} {black} {white}")
# 4615. 재미있는 오셀로 게임 D3
t = int(input())
# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    mid = n // 2
    game = []
    for i in range(n):
        game.append([0]*n)

    game[mid - 1][mid - 1] = 2
    game[mid - 1][mid] = 1
    game[mid][mid - 1] = 1
    game[mid][mid] = 2


    for j in range(m):
        x, y, s = map(int, input().split())
        if x < 0 or x >=n or y < 0 or y >= n:
            continue
        else:
            game[y][x] = s

        for k in range(n):

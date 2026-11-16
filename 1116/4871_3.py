# 4871. [S/W 문제해결 기본] 4일차 - 그래프 경로 D2
t = int(input())

for test_case in range(1, t+1):
    v, e = map(int, input().split())
    a = []

    for i in range(e):
        a.append(list(map(int, input().split())))

    score = []
    for k in range(v+1):
        score.append([])

    for j in a:
        start = j[0]
        end = j[1]
        score[start].append(end)

    s, g = map(int, input().split())
    answer = 0

    visited = [False] * (v+1)
    def dfs(now):
        visited[now] = True

        for next_node in score[now]:
            if visited[next_node]==False:
                dfs(next_node)

    dfs(s)

    if visited[g] ==True:
        answer = 1

    print(f"#{test_case} {answer}")
# 4871. [S/W 문제해결 기본] 4일차 - 그래프 경로 D2
t = int(input())

for test_case in range(1, t+1):
    v, e = map(int, input().split())
    a = []
    for i in range(e):
        a.append(list(map(int, input().split())))

    node = []
    for i in range(v+1):
        node.append([])

    for j, k in a:
        node[j].append(k)

    visited = [False] * (v+1)
    answer = "0"
    s, g = map(int, input().split())

    def dfs(s):
        visited[s] = True

        for next_node in node[s]:
            if visited[next_node] == False:
                dfs(next_node)


    dfs(s)

    if visited[g] == True:
        answer = "1"

    print(f'#{test_case} {answer}')
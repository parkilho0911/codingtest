# 4871번 [S/W 문제해결 기본] 4일차 - 그래프 경로
t = int(input())

for test_case in range(1, t+1):
    v, e = map(int, input().split()) # 2. 간선 정보를 e번 입력받아, 출발 노드에 도착 노드를 저장한다.

    a = []  # 1번 빈 리스트 만들기
    for i in range(v + 1):
        a.append([])

    for i in range(e): # 3. 탐색할 출발점 s와 도착점 g를 한 번 입력받는다.
        start, end = map(int, input().split())
        a[start].append(end)

    # 출발점과 도착점
    s, g = map(int, input().split())

    # 처음에는 모든 노드를 방문하지 않은 상태입니다.
    visited = [False] * (v + 1)

    # 현재 노드를 방문하고, 연결된 노드들을 탐색합니다.
    def dfs(now):
        visited[now] = True

        # 현재 노드에서 갈 수 있는 노드를 하나씩 꺼냅니다.
        for next_node in a[now]:
            if visited[next_node] == False:
                dfs(next_node)
    # 출발점에서 갈 수 있는 노드들을 방문합니다.
    dfs(s)

    # 탐색 후 도착점을 방문했는지 확인합니다.
    if visited[g] == True:
        answer = 1
    else:
        answer = 0

    print(f"#{test_case} {answer}")




















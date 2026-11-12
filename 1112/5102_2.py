# 5102. [S/W 문제해결 기본] 6일차 - 노드의 거리 D2
from collections import deque
t = int(input())

for test_case in range(1, t+1):
    v, e = map(int, input().split())

    a= []
    for i in range(v+1):
        a.append([])

    for i in range(e):
        start, end = map(int, input().split())
        a[start].append(end)
        a[end].append(start)

    def bfs(s):
        distance = [-1] * (v+1)

        distance[s] = 0

        queue = deque([s])

        while queue:
            now = queue.popleft()

            for next_node in a[now]:
                if distance[next_node] == -1:
                    distance[next_node] = distance[now] + 1

                    queue.append(next_node)
        if distance[g] == -1:
            return 0


        return distance[g]
    answer = bfs(start)
    print(f"#{test_case} {answer}")
    
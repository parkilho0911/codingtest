# 5248. [S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
from collections import deque
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())

    a = []
    for i in range(n+1):
        a.append([])

    people = list(map(int, input().split()))

    for j in range(0, len(people), 2):
        start = a[j]
        end = a[j+1]

        a[start].append(end)
        a[end].append(start)

    visited = [False] * (n+1)

    def bfs(s):
        visited[s] = True

        queue = deque(s)

        while queue:
            now = queue.popleft()

            for next_node in a[now]:
                if visited[next_node] == False:
                    visited[next_node] = True

                    queue.append(next_node)


    count = 0
    for k in range(1, n+1):
        if visited[k] == False:
            count += 1

            bfs(k)
    print(f"#{test_case} {count}")
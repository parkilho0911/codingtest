# 5248. [S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
from collections import deque
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    total = []
    for i in range(n+1):
        total.append([])

    for j in range(0, len(a), 2):
        start = a[j]
        end = a[j+1]
        total[start].append(end)
        total[end].append(start)

    visited = [False] * (n+1)
    count = 0

    def bfs(s):
        visited[s] = True
        queue = deque([s])

        while queue:
            now = queue.popleft()
            for k in total[now]:
                if visited[k] == False:
                    visited[k] = True
                    queue.append(k)

    for h in range(1, n+1):
        if visited[h] == False:
            count += 1
            bfs(h)
    print(f"#{test_case} {count}")
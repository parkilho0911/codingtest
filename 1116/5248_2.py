# 5248. [S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
from collections import deque
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    b = []
    for k in range(n+1):
        b.append([])

    for i in range(0, len(a), 2):
        start = a[i]
        end = a[i+1]
        b[start].append(end)
        b[end].append(start)

    visited = [False] * (n+1)
    def bfs(s):
        visited[s] = True

        queue = deque([s])

        while queue:
            now = queue.popleft()

            for next_node in b[now]:
                if not visited[next_node]:
                    visited[next_node] = True

                    queue.append(next_node)

        return 0


    # 사람 번호 1부터 n까지 확인한다.
    for h in range(1, n + 1):
        # 아직 방문하지 않았다면 새로운 그룹이다.
        if not visited[h]:
            count += 1

            # 같은 그룹에 속한 사람들을 모두 방문 처리한다.
            bfs(h)

    # 전체 그룹 수를 출력한다.
    print(f"#{test_case} {count}")
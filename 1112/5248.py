# 5248. [S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
from collections import deque
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())

    a = []
    for i in range(n +1):
        a.append([])
    # people는 사람의 숫자를 리스트로 넣는 것
    people = list(map(int, input().split()))

    for j in range(0, len(people), 2):
        start = people[j]
        end = people[j+1]

        a[start].append(end)
        a[end].append(start)

    visited = [False] * (n+1)

    def bfs(s):
        visited[s] = True
        queue = deque([s])

        while queue:
            now = queue.popleft()

            for next_node in a[now]:
                if visited[next_node] == False:
                    visited[next_node] = True
                    queue.append(next_node)

    # 이번 테스트케이스의 팀 개수입니다.
    count = 0

    # 1번부터 n번 사람까지 확인합니다.
    for person in range(1, n + 1):
        # 아직 방문하지 않았다면 새로운 팀입니다.
        if visited[person] == False:
            count += 1

            # 같은 팀 사람들을 모두 방문 처리합니다.
            bfs(person)

    # 모든 사람을 확인한 뒤 팀 개수를 출력합니다.
    print(f"#{test_case} {count}")
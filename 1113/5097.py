# 5097. [S/W 문제해결 기본] 6일차 - 회전 D2
from collections import deque
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = deque(a)
    for i in range(m):
        first = b.popleft()
        b.append(first)

    answer = b.popleft()
    print(f"#{test_case} {answer}")

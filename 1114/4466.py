# 4466. 최대 성적표 만들기 D3
t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    a.sort()
    for i in range(k):
        max_a = max(a)
        total += max_a
        a.pop()
    print(f"#{test_case} {total}")
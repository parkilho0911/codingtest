# 6485. 삼성시의 버스 노선 D3
t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    p = int(input())

    total = [0] * 5001
    answer = []
    for i in a:
        start = i[0]
        end = i[1]

        for stop in range(start, end+1):
            total[stop] += 1


    for j in range(p):
        c = int(input())
        answer.append(total[c])

    print(f"#{test_case}", *answer)

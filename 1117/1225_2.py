t = 10

for test_case in range(1, t+1):
    n = int(input())

    a = list(map(int, input().split()))
    total = 0
    answer = []
    while a[7] > 0:
        for i in range(1, 6):
            total = a[0] - i
            a.pop(0)

            if total <= 0:
                a.append(0)
                break

            a.append(total)
    print(f"#{test_case}", *a)
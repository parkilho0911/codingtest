# 1289. 원재의 메모리 복구하기 D3
t = int(input())

for test_case in range(1, t+1):
    n = list(map(int, input().strip()))

    total = [0] * len(n)

    count = 0
    for i in range(len(n)):
        if n == total:
            break

        if n[i] != total[i]:
            if n[i] == 1:
                total[i:] = [1] * (len(total) - i)
            elif n[i] == 0:
                total[i:] = [0] * (len(total) - i)
            count += 1

    print(f"#{test_case} {count}")
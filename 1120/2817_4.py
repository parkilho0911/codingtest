# 2817. 부분 수열의 합 D3
t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    total = [0]
    sum_a = 0
    count = 0

    for i in range(n):
        length = len(total)

        for j in range(length):
            sum_a = total[j] + a[i]
            if sum_a <= k:
                total.append(sum_a)

    for g in total:
        if g == k:
            count +=1

    print(f"#{test_case} {count}")
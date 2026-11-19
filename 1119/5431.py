# 5431. 민석이의 과제 체크하기 D3
t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    student = [False] * (n+1)
    total = []

    for i in a:
        student[i] = True

    for j in range(1, n+1):
        if student[j] == True:
            continue
        else:
            total.append(j)
    print(f"#{test_case}", *total)
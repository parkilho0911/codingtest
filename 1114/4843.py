# 4843. [S/W 문제해결 기본] 2일차 - 특별한 정렬 D3
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    total0 = []
    total1 = []
    len_a = len(a)//2
    answer = []
    a.sort()
    for i in range(0, len_a):
        total0.append(a[i])
        # 1 2 3 4 5

    for j in range(len_a, len(a)):
        total1.append(a[j])
        # 6 7 8 9 10 <- 이거는 sort(reverse=True)이게 필요함

    total1.sort(reverse=True)

    for k in range(len_a):
        answer.append(total1[k])
        answer.append(total0[k])

    print(f"#{test_case}", *answer[:10])

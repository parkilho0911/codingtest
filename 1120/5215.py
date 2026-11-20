# 5215. 햄버거 다이어트 D3
t = int(input())

for test_case in range(1, t+1):
    N, L = map(int, input().split())

    a = []
    kcal_total = [0]
    taste_total = [0]
    kcal = 0
    taste = 0
    for i in range(N):
        a.append(list(map(int, input().split())))
    # a[0][0]에는 맛의 점수 a[0][1]에는 칼로리
    for j in range(N):
        length = len(kcal_total)
        length_2 = len(taste_total)
        for k in range(length):
            kcal = kcal_total[k] + a[j][1]
            taste = taste_total[k] + a[j][0]
            if kcal <= L:
                kcal_total.append(kcal)
                taste_total.append(taste)

    answer = max(taste_total)
    print(f"#{test_case} {answer}")


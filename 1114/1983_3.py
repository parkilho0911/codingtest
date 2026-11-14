# 1983. 조교의 성적 매기기 D2
t = int(input())

for test_case in range(1, t+1):
    N,M = map(int, input().split())
    a = []
    score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    for i in range(N):
        a.append(list(map(int, input().split())))
    # 중간 35퍼 + 기말 45퍼 + 과제 20퍼
    total = [] # 큰 숫자부터 정렬함
    sum_a = [] # 합계를 인덱스 순서에 맞게 넣음
    for j in range(N):
        a_sum = a[j][0] * 35 + a[j][1] * 45 + a[j][2] * 20

        total.append(a_sum)
        sum_a.append(a_sum)

    total.sort(reverse=True)
    target = sum_a[M - 1]
    # total은 합계가 높은 것부터 정렬이 되어있음 5 3 2 1
    # a는 그냥 처음에 입력 받았던 합계들  1 3 2 5
    # 근데 결국 원하는거는 a[k]의 값이 score의 어떤 값을 반환하는가?
    rank = total.index(target)
    grade_idx = rank // (N // 10)

    answer = score[grade_idx]
    print(f"#{test_case} {answer}")

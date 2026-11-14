# 1221. [S/W 문제해결 기본] 5일차 - GNS D3
t = int(input())

for test_case in range(1, t+1):
    m, n = map(str, input().split())
    a = list(map(str, input().split()))
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count = [0] * 10
    total = []
    answer = []

    for i in a:
        if i == "ZRO":
            count[0] += 1
        if i == "ONE":
            count[1] += 1
        if i == "TWO":
            count[2] += 1
        if i == "THR":
            count[3] += 1
        if i == "FOR":
            count[4] += 1
        if i == "FIV":
            count[5] += 1
        if i == "SIX":
            count[6] += 1
        if i == "SVN":
            count[7] += 1
        if i == "EGT":
            count[8] += 1
        if i == "NIN":
            count[9] += 1

    # 숫자 크기순으로 확인합니다.
    for j in range(10):
        # 등장한 횟수만큼 단어 하나씩 추가합니다.
        for k in range(count[j]):
            total.append(number[j])

    print(f"#{test_case}")
    print(*total)

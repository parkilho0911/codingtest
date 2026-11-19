# 6190. 정곤이의 단조 증가하는 수 D3
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    total = []
    score = 0

    for i in range(len(a)):
        for j in range(1+i, n):
            score = a[i] * a[j]
            total.append(str(score))

    answer = []
    for k in range(len(total)):
        number = total[k]
        is_valid = True

        for p in range(len(number) - 1):
            if number[p] > number[p+1]:
                is_valid = False
                break
        if is_valid == True:
            answer.append(int(number))
    if answer:
        max_answer = max(answer)
    else:
        answer = -1
    print(f"#{test_case} {max_answer}")
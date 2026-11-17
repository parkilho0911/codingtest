# 4406. 모음이 보이지 않는 사람 D3
t = int(input())

for test_case in range(1, t+1):
    a = list(input().strip())

    b = ["a", "e", "i", "o", "u"]
    total = []
    answer = ""
    for i in b:
        for j in range(len(a)):
            if i == a[j]:
                total.append(j)

    total.sort(reverse=True)
    for k in total:
        a.pop(k)

    for h in a:
        answer += h
    print(f"#{test_case} {answer}")
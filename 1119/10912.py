# 10912. 외로운 문자 D3
t = int(input())

for test_case in range(1, t+1):
    n = list(input())

    total = []
    answer = ""
    i = 0
    while i < len(n):
        j = i + 1

        while j < len(n) and n[i] != n[j]:
            j += 1

        if j < len(n):
            n.pop(j)
            n.pop(i)
        else:
            i += 1

    n.sort()

    if n:
        for k in n:
            answer += k
    else:
        answer = "Good"

    print(f"#{test_case} {answer}")
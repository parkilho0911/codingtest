# 11856. 반반 D3
t = int(input())

for test_case in range(1, t+1):
    s = list(input())

    count = 0
    for i in range(3):
        for j in range(1+i, 4):
            if s[i] == s[j]:
                count += 1

    if count == 2:
        answer = "Yes"
    else:
        answer = "No"

    print(f"#{test_case} {answer}")
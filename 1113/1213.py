# 1213. [S/W 문제해결 기본] 3일차 - String D3
t = 10

for test_case in range(1, t+1):
    case_number = int(input())
    n = input()
    a = input()

    count = 0
    a_len = len(a)
    for i in range(a_len):
        if i+len(n) <= a_len:
            if a[i] == n[0]:
                if a[i:i+len(n)] == n:
                    count += 1

    print(f"#{test_case} {count}")

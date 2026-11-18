# 4834. [S/W 문제해결 기본] 1일차 - 숫자 카드 D2
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    a = input()

    b = []
    for i in a:
        b.append(int(i))

    count = [0] * 10

    for i in b:
        count[i] += 1

    max_number = count.index(max(count))
    max_count = max(count)

    for number in range(10):
        if count[number] == max_count and number > max_number:
            max_number = number

    print(f"#{test_case} {max_number} {max_count}")
# 2817. 부분 수열의 합 D3
t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    # 아무것도 선택하지 않은 합 0부터 시작한다.
    total = [0]
    count = 0

    # 숫자를 하나씩 처리한다.
    for i in range(n):
        # 이번 숫자를 더하기 전까지 만들어진 합의 개수를 기억한다.
        length = len(total)

        for j in range(length):
            # 기존 선택에 이번 숫자를 추가한 합을 만든다.
            new_total = total[j] + a[i]

            # 모든 숫자가 양수이므로 k를 초과한 합은 보관하지 않는다.
            if new_total <= k:
                total.append(new_total)

                # 목표 합을 만드는 선택을 찾았으면 센다.
                if new_total == k:
                    count += 1

    print(f"#{test_case} {count}")
# 2805. 농작물 수확하기 D3
t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    a = []
    for i in range(n):
        a.append(list(map(int, input().strip())))

    cut = n//2
    total = 0

    for row in range(cut):
        for col in range(cut-row, cut+row+1):
            total += a[row][col]

    for row_2 in range(n-cut):
        for col_2 in range(0+row_2, n-row_2):
            total += a[cut + row_2][col_2]

    print(f"#{test_case} {total}")


#2805 농작물 수확하기
t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    a = []
    total = 0
    half = n//2
    for i in range(n):
        a.append(list(map(int, input().strip())))
    # 1번 마름모를 구하는 방식을 찾아야함
    # 그래서 생각한게 n을 //2로 한 다음 for문을 2개 돌려서 하나는 위에서부터 반까지 가는거고
    # 하나는 밑에서부터 반 전까지 올라오는 것
    # 첫 행부터 가운데 행까지 확인합니다.
    for row_1 in range(half + 1):

        # 현재 행에서 수확할 열의 시작과 끝을 구합니다.
        left = half - row_1
        right = half + row_1

        # right 열까지 포함하려고 끝값에 1을 더합니다.
        for col in range(left, right + 1):
            total += a[row_1][col]  # 현재 행의 선택된 칸을 더합니다.

    for row_2 in range(1, half + 1):

        left = 0 + row_2
        right = n - 1 - row_2

        for col in range(left, right + 1):
            total += a[half+row_2][col]  # 현재 행의 선택된 칸을 더합니다.

    print(f"#{test_case} {total}")

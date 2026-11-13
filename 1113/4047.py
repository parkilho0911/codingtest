# 4047. 영준이의 카드 카운팅
t = int(input())

for test_case in range(1, t + 1):
    a = input()

    # 무늬별 1~13번 카드의 보유 여부입니다. 0번은 사용하지 않습니다.
    s = [False] * 14
    d = [False] * 14
    h = [False] * 14
    c = [False] * 14

    # 카드 목록, 중복 여부, 부족한 개수를 저장합니다.
    total = []
    answer = ""
    l = []

    # 3글자씩 잘라 카드 한 장으로 저장합니다.
    for i in range(0, len(a), 3):
        total.append(a[i:i + 3])

    # 카드마다 무늬와 번호를 확인합니다.
    for j in total:
        suit = j[0]
        number = int(j[1:3])

        # 이미 True인 카드가 다시 나오면 중복입니다.
        if suit == "S":
            if s[number] == True:
                answer = "ERROR"
                break
            s[number] = True

        elif suit == "D":
            if d[number] == True:
                answer = "ERROR"
                break
            d[number] = True

        elif suit == "H":
            if h[number] == True:
                answer = "ERROR"
                break
            h[number] = True

        elif suit == "C":
            if c[number] == True:
                answer = "ERROR"
                break
            c[number] = True

    # S 카드의 부족한 개수를 저장합니다.
    count = 0
    for z in range(1, 14):
        if s[z] == False:
            count += 1
    l.append(count)

    # D 카드의 부족한 개수를 저장합니다.
    count = 0
    for x in range(1, 14):
        if d[x] == False:
            count += 1
    l.append(count)

    # H 카드의 부족한 개수를 저장합니다.
    count = 0
    for y in range(1, 14):
        if h[y] == False:
            count += 1
    l.append(count)

    # C 카드의 부족한 개수를 저장합니다.
    count = 0
    for v in range(1, 14):
        if c[v] == False:
            count += 1
    l.append(count)

    # 중복이면 ERROR를 출력하고 다음 테스트케이스로 넘어갑니다.
    if answer == "ERROR":
        print(f"#{test_case} ERROR")
        continue

    # S, D, H, C 순서로 부족한 개수를 출력합니다.
    print(f"#{test_case}", *l)

# 하드코딩이 아닌 방법
# 테스트케이스 개수를 입력받습니다.
# t = int(input())
#
# for test_case in range(1, t + 1):
#     a = input()
#
#     # 무늬 이름으로 각 보유 여부 배열을 선택할 수 있게 묶습니다.
#     cards = {
#         "S": [False] * 14,
#         "D": [False] * 14,
#         "H": [False] * 14,
#         "C": [False] * 14,
#     }
#
#     # 중복 여부를 기록합니다.
#     error = False
#
#     # 카드 한 장씩 잘라서 바로 확인합니다.
#     for i in range(0, len(a), 3):
#         card = a[i:i + 3]
#         suit = card[0]
#         number = int(card[1:3])
#
#         # 해당 무늬와 번호의 카드가 이미 있다면 중복입니다.
#         if cards[suit][number] == True:
#             error = True
#             break
#
#         # 처음 나온 카드라면 보유 표시합니다.
#         cards[suit][number] = True
#
#     # 중복이면 정상 개수 계산을 건너뜁니다.
#     if error:
#         print(f"#{test_case} ERROR")
#         continue
#
#     # 무늬 순서대로 부족한 개수를 계산합니다.
#     answer = []
#     for suit in "SDHC":
#         count = 0
#
#         # 아직 없는 카드만 셉니다.
#         for number in range(1, 14):
#             if cards[suit][number] == False:
#                 count += 1
#
#         # 무늬 하나의 최종 개수를 저장합니다.
#         answer.append(count)
#
#     # S, D, H, C 순서로 출력합니다.
#     print(f"#{test_case}", *answer)
# 4873. [S/W 문제해결 기본] 4일차 - 반복문자 지우기 D2
# 과정 : 문자를 리스트로 입력을 받아서 리스트의 i와 i+1이 서로 같다면 둘다 pop을 사용해서 없앤다

t = int(input())

for test_case in range(1, t+1):
    ch = list(map(str, input().strip()))
    i = 0

    while i < len(ch) - 1:
        if ch[i] == ch[i+1]:
            ch.pop(i+1)
            ch.pop(i)

            if i > 0:
                i -= 1
        else:
            i += 1

    print(f"#{test_case} {len(ch)}")
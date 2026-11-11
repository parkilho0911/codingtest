# 4866번 [S/W 문제해결 기본] 4일차 - 괄호검사 D2
t = int(input())

for test_case in range(1, t+1):
    a = input()
    stack = [] #빈 배열을 만들어서 a안에서 괄호에 대한 정보를 저장할 수 있도록 한다
    answer = 1

    for ch in a:
        if ch == "(" or ch == "{":
            stack.append(ch)
        elif ch == ")":
            if len(stack) == 0:
                answer = 0
                break
            if stack[-1] != "(":
                answer = 0
                break
            stack.pop()
        elif ch == "}":
            # 여는 괄호가 없다면 실패입니다.
            if len(stack) == 0:
                answer = 0
                break

            # 마지막 여는 괄호가 {가 아니면 실패입니다.
            if stack[-1] != "{":
                answer = 0
                break

            # 짝이 맞으면 마지막 괄호를 제거합니다.
            stack.pop()
    if len(stack) > 0:
        answer = 0

    print(f"#{test_case} {answer}")

# 11315. 오목 판정 D3
# 가로,세로에서 연속되는 5개가 있는지 판단하고
# 그 다음 왼쪽 대각선과 오른쪽 대각선이 연속 5개가 되는지 판단하자
# 테스트케이스 개수를 입력받습니다.
t = int(input())

# 오른쪽, 아래, 오른쪽 대각선, 왼쪽 대각선
dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

for test_case in range(1, t+1):
    n = int(input())
    answer = "NO"
    a = []
    for i in range(n):
        a.append(list(input()))

    for row in range(n):
        for col in range(n):

            for j in range(4):
                count = 0

                for k in range(5):
                    nx = row + dx[j] * k
                    ny = col + dy[j] * k

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        break

                    if a[nx][ny] != "o":
                        break
                    count += 1

                    if count == 5:
                        answer = "YES"
    print(f"#{test_case} {answer}")

# 5789. 현주의 상자 바꾸기 D3
t = int(input())

for test_case in range(1, t+1):
    n, q = map(int, input().split())

    a = [0] * (n+1)

    for k in range(1, q+1):
        l, r = map(int, input().split())

        for i in range(l, r+1):
            a[i] = k
    a.pop(0)

    print(f"#{test_case}", *a)
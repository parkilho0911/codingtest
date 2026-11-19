# 10570. 제곱 팰린드롬 수 D3
t = int(input())

for test_case in range(1, t+1):
    a, b = map(int, input().split())

    p = []
    for i in range(a, b+1):
        p.append(i)
    count = 0

    for j in p:
        total = []
        for k in range(1, b+1):
           if k * k > j:
              break

           if k * k == j:
              j_text = str(j)
              k_text = str(k)

              if j_text == j_text[::-1] and k_text == k_text[::-1]:
                 count += 1
              break

    print(f"#{test_case} {count}")
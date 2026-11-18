# 1289. 원재의 메모리 복구하기 D3
t = int(input())

for test_case in range(1, t+1):
    n = input()

    a = []
    for i in n:
        a.append(int(i)) # 지피티에게 int만 도움 받음

    count = 0

    bit = [0] * len(n)
    # 결국 a리스트에 들어있는 것처럼 bit를 만들어야 해
    for j in range(len(n)):
        if a == bit:
            break

        if a[j] == bit[j]:
            continue
        else:
            if a[j] == 1:
                for k in range(j, len(n)):
                    bit[k] = 1
            else:
                for k in range(j, len(n)):
                    bit[k] = 0
        count += 1

    print(f"#{test_case} {count}")
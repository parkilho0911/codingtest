#1289번 원재의 메모리 복구하기
#힌트 후 해결
t = int(input())

for test_case in range(1,t+1):
    n = input().strip()
    total = []
    a = len(n)
    answer = [0]*a
    count = 0
    for i in n:
        total.append(int(i))

    for j in range(a):
        if answer[j] !=total[j]:
            for k in range(j,a):
                answer[k] = total[j]
            count +=1


    print(f"#{test_case} {count}")
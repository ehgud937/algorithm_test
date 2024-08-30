t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    result = bin(k)[-1: -n-1 : -1]
    cnt = 0
    answer = 'OFF'

    for i in range(len(result)):
        if result[i] == '1':
            cnt += 1

    if cnt == n:
        answer = 'ON'

    print(f'#{tc} {answer}')
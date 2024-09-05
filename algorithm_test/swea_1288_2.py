t = int(input())

for tc in range(1, t+1):
    N = int(input())
    n = 0
    ans = []
    result = []
    while True:
        n += 1
        now = n * N
        current = str(now)
        for i in current:
            result.append(int(i))
        result = list(set(result))
        if len(result) == 10:
            ans = now
            break
    print(f'#{tc} {ans}')
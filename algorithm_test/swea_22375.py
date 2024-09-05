t = int(input())

for tc in range(1, t+1):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    n = 0
    i = 0

    while i <  N:
        if before[i] != after[i]:
            n += 1
            for j in range(i, N):
                before[j] = 1 - before[j]
        if before == after:
            break
        i += 1

    print(f'#{tc} {n}')
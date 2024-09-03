t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_v = 99999

    for i in range(1, N-1):
        for j in range(i+1, N):
            w = b = r = 0
            for k in range(0, i):
                w += M - arr[k].count('W')
            for p in range(i, j):
                b += M - arr[p].count('B')
            for l in range(j, N):
                r += M - arr[l].count('R')

            min_v = min(min_v, w + b + r)
    print(f'#{tc} {min_v}')
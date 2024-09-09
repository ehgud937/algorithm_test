direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = 0
    j = -1
    n = 1

    while n <= N*N:
        for di, dj in direction:
            ni = i + di
            nj = j + dj
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = n
                n += 1
                i = ni
                j = nj
                ni += di
                nj += dj
    for i in arr:
        print(*i)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def find(i, j):
    global ans
    for di, dj in direction:
        cnt = 0
        ni = i + di
        nj = j + dj
        while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
            cnt += 1
            ni += di
            nj += dj

        if cnt == 4:
            ans = 'YES'

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                find(i, j)
    print(f'#{tc} {ans}')
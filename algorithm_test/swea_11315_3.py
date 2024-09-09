direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for di, dj in direction:
                    cnt = 1
                    ni = i + di
                    nj = j + dj
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di
                        nj += dj
                    if cnt >= 5:
                        ans = 'YES'
    print(f'#{tc} {ans}')
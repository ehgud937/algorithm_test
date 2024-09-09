di = [0, 1]
dj = [1, 0]

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                garo = 1
                sero = 1

                for k in range(1):
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                        garo += 1
                        ni += di[k]
                        nj += dj[k]
                for k in range(1, 2):
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                        sero += 1
                        ni += di[k]
                        nj += dj[k]
                max_v = max(max_v, (garo * sero))

    print(f'#{tc} {max_v}')
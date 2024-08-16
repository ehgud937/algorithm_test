t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    di = [0, 1, 0, -1]
    dj = [1, 0 ,-1, 0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < n and 0 <= nj < n:
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'B':
                for k in range(4):
                    for l in range(1, 3):
                        ni = i + (di[k] * l)
                        nj = j + (dj[k] * l)
                        if 0 <= ni < n and 0 <= nj < n:
                            arr[ni][nj] = 'X'
            elif arr[i][j] == 'C':
                for k in range(4):
                    for l in range(1, 4):
                        ni = i + (di[k] * l)
                        nj = j + (dj[k] * l)
                        if 0 <= ni < n and 0 <= nj < n:
                            arr[ni][nj] = 'X'
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_cnt = 0

    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                for p in range(1, n):
                    ni = i + (di[k] * p)
                    nj = j + (dj[k] * p)
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt += arr[ni][nj]
            cnt += arr[i][j]
            if cnt > max_cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')
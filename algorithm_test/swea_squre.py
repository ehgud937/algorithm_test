t = int(input())

di = [0, 1]
dj = [1, 0]
 
for tc in range(1, t+1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_extent = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                garo = 1
                sero = 1
                for k in range(1):
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
                        garo += 1
                        arr[ni][nj] = 0
                        ni = ni + di[k]
                        nj = nj + dj[k]
                        
                for k in range(1,2):
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
                        sero += 1
                        arr[ni][nj] = 0
                        ni = ni + di[k]
                        nj = nj + dj[k]
                if (garo * sero) > max_extent:
                    max_extent = (garo * sero)
    print(f'#{tc} {max_extent}')
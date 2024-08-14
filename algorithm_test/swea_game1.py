t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [[0] * n for _ in range(n)]

    arr[n // 2][n // 2] = 2
    arr[n // 2 - 1][n // 2 - 1] = 2
    arr[n // 2 - 1][n // 2] = 1
    arr[n // 2][n // 2 - 1] = 1


    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]


    for _ in range(m):
        j, i, color = map(int, input().split())
        i -= 1
        j -= 1

        if color == 1:  # 흑돌
            arr[i][j] = 1
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                stack = []
                while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 2:
                    stack.append((ni,nj))
                    ni, nj = ni + di[k], nj + dj[k]
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
                    for a, b in stack:
                        arr[a][b] = 1


        if color == 2:  # 백돌
            arr[i][j] = 2
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                stack = []
                while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
                    stack.append((ni, nj))
                    ni, nj = ni + di[k], nj + dj[k]
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 2:
                    for a, b in stack:
                        arr[a][b] = 2
    b = 0
    w = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                b += 1
            if arr[i][j] == 2:
                w += 1

    print(f'#{tc} {b} {w}')
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    i, j = 99, arr[99].index(2)
    di, dj = [0, 0, -1], [-1, 1, 0]

    while i > 0:
        for k in range(3):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1:
                # arr[i][j] = 0
                i, j = ni, nj
                break

    print(f'#{tc} {j}')
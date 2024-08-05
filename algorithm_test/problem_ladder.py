for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    i = 99
    j = arr[-1].index(2)

    di = [0, -1, 0]
    dj = [1, 0, -1]

    while i > 0:
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                i, j = ni, nj
    print(f'#{tc} {j}')
t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    i, j, num = 0, -1, 1

    while num <= n*n:
        for d in dir:
            while 0 <= i + d[0] < n and 0 <= j + d[1] < n:
                if arr[i + d[0]][j + d[1]] != 0:
                    break
                i += d[0]
                j += d[1]
                arr[i][j] = num
                num += 1
    print(f'#{tc}')
    for result in arr:
        print(*result)
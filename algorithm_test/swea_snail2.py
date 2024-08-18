t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    direction = [(0,1), (1,0), (0,-1), (-1,0)]

    i, j = 0, -1
    num = 1

    while n*n >= num:
        for d in direction:
            while 0 <= i+d[0] < n and 0 <= j + d[1] < n and arr[i+d[0]][j + d[1]] == 0:
                arr[i+d[0]][j+d[1]] = num
                i += d[0]
                j += d[1]
                num += 1
    for i in arr:
        print(*i)
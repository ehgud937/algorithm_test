def bfs(i, j):
    q = [(i, j)]

    while q:
        i, j = q.pop()

        for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni = i + k[0]
            nj = j + k[1]

            if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                q.append((ni, nj))



t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    arr = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    
    result = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)
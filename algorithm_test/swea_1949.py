def dfs(i, j, s, k):
    global max_length
    visited[i][j] = 1

    if max_length < s:
        max_length = s

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
            if arr[i][j] > arr[ni][nj]:
                dfs(ni, nj, s+1, k)
            elif arr[i][j] > arr[ni][nj] - k:
                orgin = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                dfs(ni, nj, s+1, 0)
                arr[ni][nj] = orgin

    visited[i][j] = 0

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    max_length = 0
    max_height = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_height:
                max_height = arr[i][j]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_height:
                dfs(i, j, 1, k)

    print(f'#{tc} {max_length}')
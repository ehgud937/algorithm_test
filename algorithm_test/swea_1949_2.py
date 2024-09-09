direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(i, j, K, n):
    global max_v

    if max_v < n:
        max_v = n

    for di, dj in direction:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] < arr[i][j] and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, K, n+1)
            visited[ni][nj] = 0

        else:
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - K < arr[i][j] and visited[ni][nj] == 0:
                temp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] -1
                visited[ni][nj] = 1
                dfs(ni, nj, 0, n+1)
                visited[ni][nj] = 0
                arr[ni][nj] = temp

t = int(input())

for tc in range(1, t+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    visited = [[0] * N for _ in range(N)]

    top = 0
    for i in range(N):
        for j in range(N):
            if top < arr[i][j]:
                top = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, K, 1)
                visited[i][j] = 0

    print(f'#{tc} {max_v}')
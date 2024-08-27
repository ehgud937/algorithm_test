d = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

def dfs(n, current_i, current_j, visited, start_i, start_j):
    global result

    if n > 3:
        return

    if n == 3 and start_i == current_i and start_j == current_j:
        result = max(result, len(visited))
        return

    for k in range(n, min(n+2,4)):
        ni = current_i + d[k][0]
        nj = current_j + d[k][1]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in visited:
            visited.append(arr[ni][nj])
            dfs(k, ni, nj, visited, start_i, start_j)


t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = -1

    for i in range(N):
        for j in range(N):
            dfs(0, i, j, [], i, j)

    print(f'#{tc} {result}')
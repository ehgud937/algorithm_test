t = int(input())

def find_start(maze):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

def find_end(maze):
    while stack:
        i, j = stack.pop()

        if maze[i][j] == 3:
            return 1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1

    return 0

for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]


    visited = [[0] * n for _ in range(n)]
    start_i, start_j = find_start(maze)
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = 1

    print(f'#{tc} {find_end(maze)}')

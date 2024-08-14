from collections import deque

t = int(input())

def dfs_maze(maze):
    # 시작점 찾기
    start = None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i, j]

    q = deque([start])
    visited[start[0]][start[1]] = 1

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        x, y = q.popleft()

        if maze[x][y] == 3:
            return visited[x][y] -1 -1

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    return 0





for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    print(f'#{tc} {dfs_maze(maze)}')
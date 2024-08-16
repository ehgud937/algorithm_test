from collections import deque


def BFS(maze):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i, j)
    
    visited = [[0] * 16 for _ in range(16)]
    q = deque([start])
    
    x,y  = start[0], start[1]
    visited[x][y] = 1

    while q:
        i, j = q.popleft()

        if maze[i][j] == 3:
            return 1
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return 0




for _ in range(1, 11):
    tc = int(input())

    arr = [list(map(int, input())) for _ in range(16)]

    print(f'#{tc}', BFS(arr))

   
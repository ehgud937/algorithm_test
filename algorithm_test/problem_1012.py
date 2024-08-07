# t = int(input())

# for _ in range(t):
#     m, n, k = map(int, input().split())

#     cabbage = [[0] * n for _ in range(m)]

#     for _ in range(k):
#         i, j = map(int, input().split())
#         cabbage[i][j] = 1
    
#     di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
#     cnt = 0
#     larva = 0
#     for i in range(m):
#         for j in range(n):
#             for k in range(4):
#                 ni = i + di[k]
#                 nj = j + dj[k]
#                 if 0 <= ni < m and 0 <= nj < n and cabbage[i][j] != 0:
#                     cabbage[i][j] = 0
#                     i = ni
#                     j = nj
#                     cnt += 1
#         if cnt >= 1:
#             larva += 1
#             cnt = 0
#     print(larva)


def dfs(x, y, n, m, cabbage):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and cabbage[nx][ny] == 1:
                cabbage[nx][ny] = 0
                stack.append((nx, ny))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    cabbage = [[0] * n for _ in range(m)]

    for _ in range(k):
        i, j = map(int, input().split())
        cabbage[i][j] = 1
    
    larva = 0
    for i in range(m):
        for j in range(n):
            if cabbage[i][j] == 1:
                dfs(i, j, n, m, cabbage)
                larva += 1

    print(larva)   
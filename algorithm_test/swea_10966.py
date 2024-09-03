'''
3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL
'''
# from collections import deque
#
# direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
# def bfs(i, j, arr):
#     global current
#
#     visited = [[0] * M for _ in range(N)]
#     q = deque()
#     q.append((i, j))
#     visited[i][j] == 1
#
#     while q:
#         i, j = q.popleft()
#
#         if arr[i][j] == 'W':
#             current = visited[i][j]
#             return
#
#         for di, dj in direction:
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
#                 visited[ni][nj] = visited[i][j] + 1
#                 q.append((ni, nj))
#
# t = int(input())
#
# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#
#     result = 0
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'L':
#                 current = 0
#                 bfs(i, j, arr)
#                 result += current
#
#     print(f'#{tc} {result}')

# from collections import deque
#
# direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
# def bfs(q, arr, result):
#     visited = [[0] * M for _ in range(N)]
#
#     while q:
#         i, j = q.popleft()
#
#         for di, dj in direction:
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'L' and visited[ni][nj] == 0:
#                 visited[ni][nj] = visited[i][j] + 1
#                 q.append((ni, nj))
#                 result += visited[ni][nj]
#
#     return result
#
# t = int(input())
#
# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     arr = deque()
#
#     for _ in range(N):
#         arr.append(list(input()))
#
#     q = deque()
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 q.append((i, j))
#
#     result = bfs(q, arr, 0)
#
#     print(f'#{tc} {result}')

from collections import deque

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(q, arr):
    result = 0
    while q:
        i, j = q.popleft()

        for di, dj in direction:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
                result += visited[ni][nj]

    return result
t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    result = bfs(q, arr)

    print(f'#{tc} {result}')
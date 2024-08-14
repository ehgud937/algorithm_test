import itertools
#
#
# def backtrack(a, k, n):
#     c = [0] * maxcandidates
#
#     if k == n:
#         process_solution(a, k)
#
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k + 1, n)
#
# def construct_candidates(a, k, n, c):
#     c[0] = True
#     c[1] = False
#     return 2
#
# def process_solution(a, k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end = ' ')
#     print()
#
# maxcandidates = 2
# nmax = 4
# a = [0] * nmax
# num = [1, 2, 3, 4]
# backtrack(a, 0, nmax)


# print(list(itertools.permutations([1,2,3,4],2)))
# t = int(input())
#
# for tc in range(1, t+1):
#     n, k = map(int, input().split())
#     arr = list(range(1,12))
#
#     for i in range(1<<12):
#         sum_num = 0
#         cnt = 0
#         for j in range(12):
#             if i & (1<<j):
#                 sum_num += arr[j]
#                 cnt += 1
#         if sum_num == k and cnt == n:
#     print(cnt)
# # ##########
# # arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
# min_num = 0
#
# for row in arr:
#     min_num += min(row)
# print(min_num)

############
# def f(i, k, s, t): # i원소, k 집합의 크기, s i-1까지 고려된 합, t목표
#     global cnt
#     global fcnt
#     fcnt += 1
#     if i == k: # 모든 원소 고려
#         if s == t:
#             cnt += 1
#         return
#     else:
#         bit[i] = 1
#         f(i + 1, k, s + a[i], t)
#         bit[i] = 0
#         f(i + 1, k, s, t)
#
#
#
# a = list(range(1, 11))
# n = 10
#
# key = 55
# cnt = 0
# bit = [0] * n
# fcnt = 0
# f(0, n, 0, key)
# print(cnt)
# print(fcnt)

# v = int(input()) # 컴퓨터 수
# e = int(input()) # 노드 수
# cnt = 0

# def DFS(s, v):
#     global cnt
#     visited = [0] * (v+1)
#     stack = []
#     visited[s] = 1
#     visit = s

#     while True:
#         for computer in computer_list[visit]:
#             if visited[computer] == 0:
#                 stack.append(visit)
#                 visit = computer
#                 visited[computer] = 1
#                 cnt += 1
#                 break
#         else:
#             if stack:
#                 visit = stack.pop()
#             else:
#                 break
                


# computer_list = [[] for i in range(v+1)]

# for _ in range(e):
#     v1, v2 = map(int, input().split())

#     computer_list[v1].append(v2)
#     computer_list[v2].append(v1)

# DFS(1, v)
# print(cnt)



# BFS

# from collections import deque

# def BFS(list, start, visited):
#     queue = deque([start])

#     visited[start] = True
#     # 큐가 빌 때까지
#     while queue:
#         # 큐에서 하나의 원소를 뽑아서 출력
#         v = queue.popleft()
#         print(v, end=' ')
#         # 아직 방문하지 않은 인접한 원소들은 큐에 삽입
#         for i in list[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# max_item = int(input())
# node = int(input())
# visited = [False] * (max_item + 1)
# graph = [[] for _ in range(max_item + 1)]

# print(graph)
# for _ in range(node):
#     v1, v2 = map(int, input().split())

#     graph[v1].append(v2)
#     graph[v2].append(v1)

# BFS(graph, 1, visited)

# from collections import deque

# def bfs(maze):
#     # 시작점 찾기
#     start = None
#     for i in range(n):
#         for j in range(m):
#             if maze[i][j] == 2:
#                 start = (i, j)
#                 break
    
#     q = deque([start])
#     arr_visited[start[0]][start[1]] = 1
#     # 움직일 위치
#     direction = [(0,1), (1,0), (-1,0), (0,-1)]

#     while q:
#         x, y = q.popleft()
#         if maze[x][y] == 3:
#             # 시작점과, 도착점을 빼주기 -> 중간 통로 길이만 구하는 경우
#             return arr_visited[x][y] -1 -1
        
#         for di, dj in direction:
#             nx = x + di
#             ny = y + dj
            
#             if 0<= nx < n and 0 <= ny < m and arr_visited[nx][ny] == 0 and maze[nx][ny] != 1:
#                 arr_visited[nx][ny] = arr_visited[x][y] + 1
#                 q.append([nx, ny])
#     return -1   # 못 찾은 경우
        


# t = int(input())
# for tc in range(1, t+1):
#     n, m = map(int, input().split())
#     maze = [list(map(int, input())) for _ in range(n)]
#     arr_visited = [[0] * m for _ in range(n)]
    
#     print(bfs(maze))
    
arr =[1, 2, 3]
print(arr)
print(arr[::-1])
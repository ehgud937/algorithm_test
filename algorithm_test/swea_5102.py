from collections import deque

t = int(input())

def bfs(list, start, end):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()

        if v == end:
            return visited[v] - 1

        for i in list[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] += visited[v] + 1
    return 0



for tc in range(1, t+1):
    v, e = map(int, input().split())

    bfs_list = [[] for _ in range(v+1)]

    for _ in range(e):
        v1, v2 = map(int, input().split())
        bfs_list[v1].append(v2)
        bfs_list[v2].append(v1)

    start, end = map(int, input().split())


    visited = [0] * (v+1)

    print(f'#{tc} {bfs(bfs_list, start, end)}')

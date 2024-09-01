from collections import deque

def bfs(start):
    visited = [0] * (n+1)
    q = deque([start])
    visited[start] = 1
    total = 0

    while q:
        current = q.popleft()

        for i in adj[current]:
            if visited[i] == 0:
                visited[i] = visited[current] + 1
                q.append(i)
                total += visited[i]
    return total

n, v = map(int, input().split())

adj = [[] for _ in range(n+1)]


for _ in range(v):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

result = 0
min_connect = 99999


for i in range(1, n+1):
    bacon = bfs(i)
    if bacon < min_connect:
        min_connect = bacon
        result = i

print(result)

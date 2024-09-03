def dfs(n):
    visited[n] = 1

    for i in adj[n]:
        if visited[i] == 0:
            dfs(i)

t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)
    result = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            result += 1
    print(f'#{tc} {result}')
def bfs(n, k):
    q = [n]
    visited = [0] * (max_loca + 1)
    visited[n] = 1

    while q:
        current = q.pop(0)

        if current == k:
            return visited[current] -1

        for i in [current-1, current+1, current*2]:
            if 0 <= i <= max_loca and visited[i] == 0:
                visited[i] = visited[current] + 1
                q.append(i)

n, k = map(int, input().split())
max_loca = 100000

print(bfs(n, k))
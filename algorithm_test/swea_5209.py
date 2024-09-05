def per_sum(n, total):
    global min_v
    if total > min_v:
        return
    if n == N:
        min_v = total

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            per_sum(n+1, total + arr[n][i])
            visited[i] = 0

t = int(input())

for tc in range(1,t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 999999
    visited = [0] * (N+1)
    per_sum(0, 0)
    print(f'#{tc} {min_v}')
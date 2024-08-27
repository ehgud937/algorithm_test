def dfs(start):
    global cnt
    visited[start] = 1
    cnt += 1

    for i in adj[start]:
        if visited[i] == 0:
            dfs(i)
    else:
        return cnt


t = int(input())

for tc in range(1, t+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(e+2)]
    visited = [0] * (e+2)

    for i in range(0, len(arr), 2):
        adj[arr[i]].append(arr[i+1])

    cnt = 0

    result = dfs(n)

    print(f'#{tc} {result}')

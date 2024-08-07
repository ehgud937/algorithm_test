def DFS(s, V, G):
    visited = [0] * (V)
    stack = []

    visited[s] = 1
    v = s
    while True:
        for w in dfs_list[v]:
            if visited[w] == 0:
                stack.append(v)   #
                v = w
                if v == G:
                    return 1

                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return 0


for _ in range(10):
    tc, n = map(int, input().split())
    arr = list(map(int, input().split()))
    dfs_list = [[] for _ in range(100)]

    for i in range(n):
        v1, v2 = arr[i*2], arr[i*2+1]
        dfs_list[v1].append(v2)

    print(f'#{tc} {DFS(0, 100, 99)}')
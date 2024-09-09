direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y, v, i, j):
    global max_v
    global min_v
    global result
    if v >= max_v:
        max_v = v
        result.append((v,arr[i][j]))

    for di, dj in direction:
        ni = x + di
        nj = y + dj
        if 0 <= ni < N and 0 <= nj < N:
            if arr[x][y]+1 == arr[ni][nj]:
                dfs(ni, nj, v+1, i, j)
                break

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 1
    min_v = 99999
    result = []
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, i, j)
    result.sort(key = lambda x:(x[0],x[1]),  reverse=True)
    ans = 999
    max_ans = 0

    for c, s in result:
        if c >= max_ans:
            max_ans = c
            ans = s
            if ans < s:
                continue
            else:
                ans = s
        if c < max_ans:
            break

    print(f'#{tc} {ans} {max_v+1}')
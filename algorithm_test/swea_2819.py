direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(i, j , n):
    global cnt
    global result

    if n == 8:
        now = ''
        for i in current:
            now += str(i)
        result.add(now)
        return

    for di, dj in direction:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            current.append(arr[i][j])
            dfs(ni, nj, n+1)
            current.pop()

t = int(input())

for tc in range(1, t+1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = set()
    current = []

    for i in range(N):
        for j in range(N):
            dfs(i, j, 1)

    print(f'#{tc} {len(result)}')
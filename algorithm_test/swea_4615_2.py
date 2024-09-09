direction = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]

    arr[N//2-1][N//2-1] = 'W'
    arr[N//2][N//2] = 'W'
    arr[N//2-1][N//2] = 'B'
    arr[N//2][N//2-1] = 'B'

    for _ in range(M):
        i, j, c = map(int, input().split())
        i -= 1
        j -= 1

        if c == 1:  # B일 때
            arr[i][j] = 'B'
            for di, dj in direction:
                stack = []
                ni = i + di
                nj = j + dj
                while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'W':
                    stack.append((ni, nj))
                    ni += di
                    nj += dj
                if 0 <= ni < N and 0 <= nj < N:
                    stack.append((ni, nj))
                if stack and arr[stack[-1][0]][stack[-1][1]] == 'B':
                    for ii, jj in stack:
                        arr[ii][jj] = 'B'

        if c == 2:  # B일 때
            arr[i][j] = 'W'
            for di, dj in direction:
                stack = []
                ni = i + di
                nj = j + dj
                while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'B':
                    stack.append((ni, nj))
                    ni += di
                    nj += dj
                if 0 <= ni < N and 0 <= nj < N:
                    stack.append((ni, nj))
                if stack and arr[stack[-1][0]][stack[-1][1]] == 'W':
                    for ii, jj in stack:
                        arr[ii][jj] = 'W'

    ans_B = 0
    ans_W = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                ans_B += 1
            elif arr[i][j] == 'W':
                ans_W += 1

    print(f'#{tc} {ans_B} {ans_W}')
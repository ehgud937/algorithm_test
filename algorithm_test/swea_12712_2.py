direction_1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


t = int(input())

for tc in range(1, t+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(N):
            current = arr[i][j]
            current_2 = arr[i][j]
            for di, dj in direction_1:
                for p in range(1, K):
                    ni = i + (di*p)
                    nj = j + (dj*p)
                    if 0 <= ni < N and 0 <= nj < N:
                        current += arr[ni][nj]

            for di, dj in direction_2:
                for p in range(1, K):
                    ni = i + (di*p)
                    nj = j + (dj*p)
                    if 0 <= ni < N and 0 <= nj < N:
                        current_2 += arr[ni][nj]

            max_v = max(max_v, current, current_2)

    print(f'#{tc} {max_v}')
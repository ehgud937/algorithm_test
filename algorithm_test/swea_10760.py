direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def find_picture(i, j):
    global ans
    cnt = 0

    for di, dj in direction:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[i][j] > arr[ni][nj]:
            cnt += 1

    if cnt >= 4:
        ans += 1


t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(M):
            find_picture(i, j)

    print(f'#{tc} {ans}')
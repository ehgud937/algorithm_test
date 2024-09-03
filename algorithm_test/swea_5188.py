def find_min(i, j, total):
    global min_total

    if total > min_total:
        return

    if i == N-1 and j == N-1:
        min_total = min(total, min_total)
        return

    for di, dj in [(0, 1), (1, 0)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            find_min(ni, nj, total + arr[ni][nj])

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_total = 99999999
    find_min(0, 0, arr[0][0])
    print(f'#{tc} {min_total}')
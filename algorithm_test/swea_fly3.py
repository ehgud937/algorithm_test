t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di_1 = [0, 1, 0, -1]
    dj_1 = [1, 0, -1, 0]

    di_2 = [-1, -1, 1, 1]
    dj_2 = [-1, 1, -1, 1]
    
    max_kill = 0

    for i in range(n):
        for j in range(n):
            current1 = arr[i][j]
            current2 = arr[i][j]

            for k in range(4):
                for l in range(1, m):
                    ni = i + (di_1[k] * l)
                    nj = j + (dj_1[k] * l)
                    if 0 <= ni < n and 0 <= nj < n:
                        current1 += arr[ni][nj]
            for k in range(4):
                for l in range(1, m):
                    ni = i + (di_2[k] * l)
                    nj = j + (dj_2[k] * l)
                    if 0 <= ni < n and 0 <= nj < n:
                        current2 += arr[ni][nj]

            max_kill = max(max_kill, current1, current2)
    print(f'#{tc} {max_kill}') 
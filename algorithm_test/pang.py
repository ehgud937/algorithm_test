t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(n)]

    max_allergie = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(n):
        for j in range(m):
            allergie = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    allergie += balloon[ni][nj]

            allergie += balloon[i][j]

            if max_allergie < allergie:
                max_allergie = allergie
    print(f'#{tc} {max_allergie}')
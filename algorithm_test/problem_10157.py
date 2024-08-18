n, m = map(int, input().split())
k = int(input())
arr = [[0] * m for _ in range(n)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 1
i = 0
j = -1

if n * m < k:
    print(0)
    exit()

while cnt < k:
    for di, dj in direction:
        while True:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                arr[ni][nj] = cnt
                if cnt == k:
                    print(ni + 1, nj + 1)
                    exit()
                cnt += 1
                i, j = ni, nj
            else:
                break

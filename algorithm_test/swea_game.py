tc = int(input())
n, m = map(int, input().split)

arr = [[0] * n for _ in range(n)]

arr[n//2][n//2] = 2
arr[n//2-1][n//2-1] = 2
arr[n//2-1][n//2] = 1
arr[n//2][n//2-1] = 1

di = [0, 1, 0, -1, -1, -1, 1, 1]
dj = [0, 1, 0, -1, -1, 1, -1, 1]

for _ in range(12):
    i, j, color = map(int, input().split())

    if color == 1: # 흑돌
        for k in range(8):
            ni = i + di
            nj = i + dj
            if arr[ni][nj] == 2:
                arr[i][j] = 1
                arr[ni][nj] = 1
    
    if color == 2: # 백돌
        for k in range(8):
            ni = i + di
            nj = i + dj
            if arr[ni][nj] == 1:
                arr[i][j] = 2
                arr[ni][nj] = 2

b = 0
w = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            b += 1
        if arr[i][j] == 2:
            w += 1
print(f'#{tc} {b} {w}')

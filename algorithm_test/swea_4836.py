t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] += 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] >= 2:
                cnt += 1
    print(f'#{tc} {cnt}')
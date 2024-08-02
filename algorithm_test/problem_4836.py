t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    color = 0
    for _ in range(n):
        a, b, c, d, e = map(int, input().split())
        for i in range(a, c+1):
            for j in range(b, d+1):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                else:
                    color += 1
    print(f'#{tc} {color}')
t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_fly = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            v = 0

            for k in range(i, i + m):
                for p in range(j, j + m):
                    v += arr[k][p]

            if max_fly < v:
                max_fly = v

    print(f'#{tc} {max_fly}')


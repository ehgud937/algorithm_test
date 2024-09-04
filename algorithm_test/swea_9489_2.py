t = int(input())

for tc in range(1, t+1):
    N, M  = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0] * (M+1))

    max_v = 0

    for i in range(N+1):
        current = 0
        for j in range(M+1):
            if arr[i][j] == 1:
                current += 1
            else:
                if current > max_v:
                    max_v = current

                current = 0
    for i in range(N+1):
        current = 0
        for j in range(M+1):
            if arr[j][i] == 1:
                current += 1
            else:
                if current > max_v:
                    max_v = current

                current = 0

    if max_v == 1:
        max_v = 0

    print(f'#{tc} {max_v}')
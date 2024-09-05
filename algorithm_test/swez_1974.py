t = int(input())

for tc in range(1, t+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result = 1
    for i in range(N):
        garo = []
        for j in range(N):
            garo.append(arr[i][j])
        if len(set(garo)) != 9:
            cnt += 1

    for i in range(N):
        sero = []
        for j in range(N):
            sero.append(arr[j][i])
        if len(set(sero)) != 9:
            cnt += 1

    for i in range(0, N, 3):
        for j in range(0, N, 3):
            check = []
            for p in range(i, i+3):
                for k in range(j, j+3):
                    check.append(arr[p][k])
            if len(set(check)) != 9:
                cnt += 1



    if cnt >= 1:
        result = 0

    print(f'#{tc} {result}')
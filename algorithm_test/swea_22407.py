t = int(input())

for tc in range(1, t+1):
    arr = [[0] * 10 for _ in range(10)]
    N = 2

    for _ in range(N):
        r1, c1, r2, c2 = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += 1
    max_sero = 0
    max_garo = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                garo = 1
                sero = 1

                ni = i
                nj = j + 1
                while 0 <= ni < 10 and 0 <= nj < 10 and arr[ni][nj] == 2:
                    garo += 1
                    ni = ni
                    nj = nj + 1

                ni = i + 1
                nj = j
                while 0 <= ni < 10 and 0 <= nj < 10 and arr[ni][nj] == 2:
                    sero += 1
                    ni = ni + 1
                    nj = nj

                max_sero = max(sero, max_sero)
                max_garo = max(garo, max_garo)

    print(f'#{tc} {max_garo} {max_sero}')

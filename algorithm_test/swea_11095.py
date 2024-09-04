t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        start_i, end_i, start_j, end_j = map(int, input().split())
        for i in range(start_i, start_j+1):
            for j in range(end_i, end_j+1):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    cnt += 1

    print(f'#{tc} {cnt}')
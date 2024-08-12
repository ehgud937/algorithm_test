t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(n)]
    row_cnt = 0
    col_cnt = 0


    for row in arr:
        cnt = 0
        for num in row:
            if num == 1:
                cnt += 1
            else:
                if cnt == k:
                   row_cnt += 1
                   cnt = 0
                else:
                   cnt = 0
    
    col_arr = arr + [[0] * (n + 1)]
    col_arr = list(zip(*col_arr))
    
    for row in col_arr:
        cnt = 0
        for num in row:
            if num == 1:
                cnt += 1
            else:
                if cnt == k:
                    col_cnt += 1
                    cnt = 0
                else:
                    cnt = 0
    print(f'#{tc} {row_cnt + col_cnt}')

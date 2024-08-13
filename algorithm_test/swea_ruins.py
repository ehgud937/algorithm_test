t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(n)]
    max_cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(m+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0
        max_cnt = max(max_cnt, cnt)

    arr = arr + [[0] * (m+1)]
    arr_col = list(zip(*arr))

    for row in arr_col:
        cnt = 0
        for j in row:
            if j == 1:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0
        max_cnt = max(max_cnt, cnt)
    
    if max_cnt == 1:
        max_cnt = 0
        
    print(f'#{tc} {max_cnt}')
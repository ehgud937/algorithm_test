t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(n)]
    arr.append([0] * (m+1))
    
    max_cnt = 0

    for i in range(n+1):
        cnt = 0
        for j in range(m+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                    cnt = 0
                cnt = 0
    
    for i in range(m+1):
        cnt = 0
        for j in range(n+1):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                    cnt = 0
                cnt = 0
    if max_cnt == 1:
        max_cnt = 0
    
    print(f'#{tc} {max_cnt}')
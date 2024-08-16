t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    min_cnt = 9999
    
    for i in range(1, n-1):  
        for j in range(i+1, n):  
            w = b = r = 0  
            for x in range(i):
                w += m - arr[x].count('W')
            for x in range(i, j):
                b += m - arr[x].count('B')
            for x in range(j, n):
                r += m - arr[x].count('R')
                
            cnt = w + b + r
            if cnt < min_cnt:
                min_cnt = cnt
    
    print(f'#{tc} {min_cnt}')

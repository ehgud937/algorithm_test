for tc in range(1, 11):
    n = 100
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0

    for i in range(n):
        current = 0
        for j in range(n):
            if arr[j][i] == 1:
                current += 1
            
            if arr[j][i] == 2 and current >= 1:
                cnt += 1
                current = 0
        
    print(f'#{tc} {cnt}')
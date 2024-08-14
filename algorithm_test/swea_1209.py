for _ in range(1, 11):
    tc = int(input())
    n = 100
    arr = list(map(int, input().split()) for _ in range(100))
    
    col_max = 0
    row_max = 0
    cross1 = 0
    cross2 = 0


    for i in range(n):
        current = 0
        for j in range(n):
            current += arr[i][j]
        if current > row_max:
            row_max = current

    for i in range(n):
        current = 0
        for j in range(n):
            current += arr[j][i]
        if current > col_max:
            col_max = current
    
    for i in range(n):
        for j in range(n):
            if i == j:
                cross1 += arr[i][j]

    for i in range(n):
        for j in range(n):
            if 2-i == j:
                cross2 += arr[i][j]
    print(f'#{tc} {max(col_max, row_max, cross1, cross2)}')
for _ in range(10):
    t = int(input())
    n, m = 100, 100

    arr = [list(map(int, input().split())) for _ in range(100)]

    max_row, max_col, max_cross = 0, 0, 0
    for row_i in range(100):
        row_sum = 0
        for row_j in range(100):
            row_sum += arr[row_j][row_i]
        if row_sum > max_row:
            max_row = row_sum

    for col_i in range(100):
        col_sum = 0
        for col_j in range(100):
            col_sum += arr[col_i][col_j]
        if col_sum > max_col:
            max_col = col_sum

    cross_sum = 0
    for cross_i in range(100):
        for cross_j in range(100):
            if cross_i == cross_j:
                cross_sum += arr[cross_i][cross_j]

    cross_reverse_sum = 0
    for cross_reverse_i in range(100):
        for cross_reverse_j in range(100):
            if 2-cross_reverse_i == cross_reverse_j:
                cross_reverse_sum += arr[cross_reverse_i][cross_reverse_j]
    print(f'#{t} {max(max_row, max_col, cross_sum, cross_reverse_sum)}')
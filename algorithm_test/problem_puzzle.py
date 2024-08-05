t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    my_list = [list(map(int, input().split())) for _ in range(n)]

    row_count = 0
    row_list = [0] * n
    for i in range(n):
        row = 0
        for j in range(n):
            row += my_list[i][j]
        row_list[i] = row

    for i in range(n - k + 1):
        for j in range(n):
            if row_list[i] == 3:
                if my_list[i][j] + my_list[i+1][j] + my_list[i+2][j] == 3:
                    row_count += 1

    col_count = 0
    col_list = [0] * n
    for i in range(n):
        col = 0
        for j in range(n):
            col += my_list[j][i]
        col_list[i] = col
    print(row_list)
    print(col_list)
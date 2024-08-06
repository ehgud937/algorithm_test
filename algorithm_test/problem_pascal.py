t = int(input())

for tc in range(1, t+1):
    n = int(input())
    my_list = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i >= j:
                if i == j:
                    my_list[i][j] = 1
                elif j == 0:
                    my_list[i][j] = 1
                else:
                    my_list[i][j] = my_list[i-1][j-1] + my_list[i-1][j]

    result = []
    print(f'#{tc}')
    for row in my_list:
        for i in row:
            if i != 0:
                result.append(i)
        print(*result)
        result = []





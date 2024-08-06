t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    my_list = list(range(1, n+1))
    my_list = [my_list] + [[0] * n for _ in range(k)]

    for i in range(1, k + 1):
        for j in range(n):
            if j == 0:
                my_list[i][j] = 1
            else:
                my_list[i][j] = my_list[i][j-1] + my_list[i-1][j]

    print(my_list[k][n-1])
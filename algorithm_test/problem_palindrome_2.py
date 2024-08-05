t = int(input())

for tc in range(1, t+1):
    m, n = map(int, input().split())

    str_list = [list(map(str, input())) for _ in range(m)]
    result = []
    my_list = []
    for row in str_list:
        for i in range(len(row) - n + 1):
            my_list = row[i : i + n]
            if my_list == my_list[::-1]:
                result = my_list
    for row in list(zip(*str_list)):
        for i in range(len(row) - n + 1):
            my_list = row[i : i + n]
            if my_list == my_list[::-1]:
                result = my_list
    print(f'#{tc} {"".join(result)}')
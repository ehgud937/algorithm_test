for tc in range(1, 11):
    n = int(input())
    str_list = [list(map(str, input())) for _ in range(8)]
    cnt = 0
    my_list = []
    for row in str_list:
        for i in range(len(row) - n + 1):
            my_list = row[i : i + n]
            if my_list == my_list[::-1]:
                cnt += 1

    for row in list(zip(*str_list)):
        for i in range(len(row) - n + 1):
            my_list = row[i: i + n]
            if my_list == my_list[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')
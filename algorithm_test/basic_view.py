for tc in range(1, 11):
    n = int(input())
    my_list = list(map(int, input().split()))
    count = 0
    for i in range(2, n-2):
        a = 0
        b = 0
        c = 0
        d = 0
        if my_list[i] > my_list[i+1] and my_list[i] > my_list[i+2] and my_list[i] > my_list[i-1] and my_list[i] > my_list[i-2]:

            a = my_list[i] - my_list[i+1]
            b = my_list[i] - my_list[i+2]
            c = my_list[i] - my_list[i-1]
            d = my_list[i] - my_list[i-2]
            count += min(a, b, c, d)
    print(f'#{tc} {count}')

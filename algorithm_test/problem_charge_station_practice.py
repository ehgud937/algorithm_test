t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    my_list = list(map(int, input().split()))
    count = 0
    flag = 0
    flag2 = 0

    if my_list[0] > k:
        flag += 1
        flag2 += 1
        print(f'#{tc} {0}')

    if k == n:
        flag += 1
        print(f'#{tc} {1}')

    if flag2 == 0:
        if n - my_list[-1] > k:
            flag += 1
            print(f'#{tc} {0}')

    for i in range(len(my_list) - 1):

        if my_list[i+1] - my_list[i] > k:
            flag += 1
            print(f'#{tc} {0}')


    if (n//m <= n//k and flag == 0):
        count = n//k
        print(f'#{tc} {count}')

    elif flag == 0:
        print(f'#{tc} {0}')

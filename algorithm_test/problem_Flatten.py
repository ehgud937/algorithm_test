t = 10
for tc in range(1, t+1):
    n = int(input())
    my_list = list(map(int, input().split()))

    for _ in range(n):
        max_idx = 0
        min_idx = 0
        max_num = 0
        min_num = 1000000
        for idx, num in enumerate(my_list):
            if num > max_num:
                max_num = num
                max_idx = idx

            if num < min_num:
                min_num = num
                min_idx = idx
                
        my_list[max_idx] -= 1
        my_list[min_idx] += 1

    real_max = 0
    real_min = 100000000

    for num in my_list:
        if num > real_max:
            real_max = num
        if num < real_min:
            real_min = num
    print(f'#{tc} {real_max - real_min}')

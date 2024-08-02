t = int(input())

for tc in range(1, t+1):
    n = int(input())
    my_num = input()
    new_list = [0] * 100
    my_list = [0] * n
    max_num = 0
    real_idx = 0

    for i in range(len(my_num)):
        my_list[i] = my_num[i]

    for num in my_list:
        new_list[int(num)] += 1

    for idx, num in enumerate(new_list):
        if max_num <= num:
            max_num = num
            real_idx = idx
    print(f'#{tc} {real_idx} {max_num}')

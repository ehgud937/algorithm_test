t = int(input())

for tc in range(1, t+1):
    n = int(input())
    my_list = list(map(int, input().split()))
    max_num = 0
    min_num = 1000
    max_idx = 0
    min_idx = 0
    for idx, num in enumerate(my_list):
        if num >= max_num:
            max_num = num
            max_idx = idx
        if num < min_num:
            min_num = num
            min_idx = idx
    print(f'#{tc} {abs(max_idx - min_idx)}')
t = int(input())

for i in range(1, t+1):
    n = int(input())
    my_list = list(map(int, input().split()))
    max_num = -float('inf')
    min_num = float('inf')
    for num in my_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f'#{i} {max_num - min_num}')



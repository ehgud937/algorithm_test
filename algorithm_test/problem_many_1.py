t = int(input())

for tc in range(1, t+1):
    n = int(input())
    num_list = input() + '0'

    max_count, count = 0, 0

    for num in num_list:
        if num == '0':
            if max_count < count:
                max_count = count
                count = 0
        else:
            count += 1

    print(f'#{tc} {max_count}')
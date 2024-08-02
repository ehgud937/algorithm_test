t = int(input())

for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    my_list = list(map(int, input().split()))
    count = 0
    current = 0

    my_list = [0] + my_list + [n]
    print(my_list)
    for i in range(1, len(my_list)):
        if my_list[i] - my_list[i - 1] > k:
            count = 0
            break
        if my_list[i] - current > k:
            current = my_list[i - 1]
            count += 1

    if current + k < n:
        count = 0

    print(f'#{tc} {count}')
t = int(input())

for tc in range(1, t+1):
    n, m = input().split()
    n = int(n)
    m = int(m)
    my_list = list(map(int, input().split()))
    max_num = -float('inf')
    min_num = float('inf')
    for i in range(n-m+1):
        count = 0
        for j in range(i + 0, i + m):
            count += my_list[j]
        if count > max_num:
            max_num = count
        if count < min_num:
            min_num = count
    print(f'#{tc} {max_num - min_num}')
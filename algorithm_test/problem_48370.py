t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = list(range(1, 13))
    max_count = 0
    for i in range(1 << 12):
        sum_num = 0
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                sum_num += arr[j]
                cnt += 1
        if sum_num == k and cnt == n:
            max_count += 1
    print(f'#{tc} {max_count}')
t = int(input())
arr = list(range(1, 13))

for tc in range(1, t+1):
    n, k = map(int, input().split())
    result = 0
    for i in range(1<<12):
        cnt = 0
        sum_num = 0
        for j in range(12):
            if i & (1<<j):
                sum_num += arr[j]
                cnt += 1
        if cnt == n and sum_num == k:
            result += 1
    print(f'#{tc} {result}')
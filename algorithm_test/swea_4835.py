t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_max = 0
    sum_min = 99999999

    for i in range(n - m + 1):
        current_sum = 0
        for j in range(i, i + m):
            current_sum += arr[j]
        if current_sum > sum_max:
            sum_max = current_sum
        if current_sum < sum_min:
            sum_min = current_sum
    
    print(f'#{tc} {sum_max-sum_min}')
t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    step = 0

    for i in range(0, n):
        while arr[i] >= k:
            arr[i] -= k
            step += (i+1) * 2
        if i < n-1:
            arr[i+1] += arr[i]
            step += 1
        else:
            step += n+1
    print(f'#{tc} {step}')

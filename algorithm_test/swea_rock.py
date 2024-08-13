t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    for _ in range(m):
        i, k = map(int, input().split())
        
        cnt = 0
        step = 1
        while step <= k:
            if (i-1) + step > n-1 or (i-1) - step < 0:
                break
            elif arr[i-1 + step] == arr[i-1 - step]:
                arr[i-1 + step] = 1 - arr[i-1 + step]
                arr[i-1 - step] = 1 - arr[i-1 - step]
                step += 1
            else:
                step += 1
            
    print(f'#{tc}', *arr)
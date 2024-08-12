t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    i = 0
    step = 0
    current = 0
    while True:
        if arr[i] == 0:
            if i == n-1:
                step += (i + 1)
                break
            else:
                i += 1
            step += 1
        elif arr[i] > k - current:
            arr[i]= arr[i] - (k - current)
            step += ((i+1) * 2)
            current = 0
        elif arr[i] < k - current:
            current += arr[i]
            arr[i] = 0
            step += 1
            i += 1
        elif arr[i] == k - current:
            arr[i] = 0
            step += ((i+1) * 2)
            current = 0
    print(step)

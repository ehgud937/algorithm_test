t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    arr = [0] + list(map(int, input().split()))
    
    for _ in range(k):
        idx, cnt = map(int, input().split())
        num = 1
        while cnt >= num:
            if idx+num <= n and idx-num >= 1:
                if arr[idx+num] == arr[idx-num]:
                    arr[idx+num] = 1 - arr[idx+num]
                    arr[idx-num] = 1 - arr[idx-num]
            num += 1
    print(f'#{tc}', *arr[1:])


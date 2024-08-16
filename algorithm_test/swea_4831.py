t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    arr = [0] + arr + [n]

    current = 0
    cnt = 0

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > k:
            cnt = 0
            break
        elif arr[i] - current > k :
            current = arr[i-1]
            cnt += 1
   
    if current + k < n:
        cnt = 0

    print(f'#{tc} {cnt}')
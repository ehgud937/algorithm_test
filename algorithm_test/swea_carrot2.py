t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(n):
        if arr[i] % k == 0:
            cnt += ((i+1) * (arr[i] // k)) * 2
        else:
            cnt += ((i+1) * ((arr[i] // k) + 1)) * 2
    print(f'#{tc} {cnt}')
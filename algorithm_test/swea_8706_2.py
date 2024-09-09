t = int(input())

for tc in range(1, t+1):
    N, K  = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    i = 1
    n = 0

    while True:
        if arr[i] > K:
            arr[i] -= K
            n += (i*2)
        elif i == N:
            n += (N)
            break
        elif arr[i] == K:
            arr[i] = 0
            n += (i*2) + 1
            i += 1
        elif arr[i] < K:
            arr[i+1] += arr[i]
            arr[i] = 0
            n += 1
            i += 1

    print(f'#{tc} {n+1}')
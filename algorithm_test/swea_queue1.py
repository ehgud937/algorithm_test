t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    i, n = 0, 0
    result = 0

    while n < k:
        arr.append(arr[i])
        result = arr[i+1]
        i += 1
        n += 1
    print(f'#{tc} {result}')
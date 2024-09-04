t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = list(input().split())
    result = []

    if N % 2 == 0:
        for i in range(0, N//2):
            result.append(arr[i])
            result.append(arr[i+N//2])
    else:
        for i in range(0, N//2+1):
            result.append(arr[i])
            if i + (N//2) + 1 < N:
                result.append(arr[i + (N//2) + 1])


    print(f'#{tc}', *result)
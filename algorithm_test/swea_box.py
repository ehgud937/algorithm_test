t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [0] * (n+1)

    for i in range(m):
        l, r = map(int, input().split())

        for k in range(l, r+1):
            arr[k] = i+1
    
    arr.pop(0)
    print(f'#{tc}', *arr)
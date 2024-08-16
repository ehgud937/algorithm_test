t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    
    for i in range(1, n+1):
        if i not in arr:
            result.append(i)
    
    print(f'#{tc}', *result)
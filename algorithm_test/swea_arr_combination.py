t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))
    result = []

    if n <= m:
        for i in range(m):
            if i < n:
                result.append(arr_n[i])
            result.append(arr_m[i])
    if n > m:
        for i in range(n):
            result.append(arr_n[i])
            if i < m:
                result.append(arr_m[i])
        
    print(f'#{tc}', *result)
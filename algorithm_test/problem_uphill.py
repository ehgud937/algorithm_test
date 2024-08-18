t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = arr + [0]
    lst = []
    max_slope = 9999
    result = 0

    for i in range(n):
        if arr[i] <= arr[i+1]:
            lst.append(arr[i])
        else:
            lst.append(arr[i])

            if (arr[-1] + arr[0]) // len(lst) < max_slope:
                max_slope = (arr[-1] + arr[0]) // len(lst) 
                result = len(lst)
            lst = []
    
    is_slope = False

    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            is_slope = True
            break
    
    if not is_slope:
        result = 0

    print(f'#{tc} {result}')
    
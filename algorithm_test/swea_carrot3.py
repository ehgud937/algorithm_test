t = int(input())

for tc in range(1, t+1):
    n = int(input())
    
    arr = list(map(int, input().split()))
    arr.sort()
    found = False
    min_diff = 999999

    for i in range(1, n-1):
        if arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n):
            if arr[j] == arr[j-1]:
                continue
            box1 = arr[:i]
            box2 = arr[i:j]
            box3 = arr[j:]

            if len(box1) > 0 and len(box2) > 0 and len(box3) > 0:
                if len(box1) <= n//2 and len(box2) <= n//2 and len(box3) <= n//2:
                     diff = max(len(box1), len(box2), len(box3)) - min(len(box1), len(box2), len(box3))
                     min_diff = min(min_diff, diff)
                     found = True
    if found:
        print(f'#{tc} {min_diff}')
    else:
        print(f'#{tc} -1')
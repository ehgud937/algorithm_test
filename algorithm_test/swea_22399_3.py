t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    find = False
    min_v = 99999999

    for i in range(1, N-1):
        if arr[i] == arr[i-1]:
            continue
        for j in range(i+1, N):
            if arr[j] == arr[j-1]:
                continue

            box1 = arr[: i]
            box2 = arr[i : j]
            box3 = arr[j : ]

            if len(box1) > 0 and len(box2) > 0 and len(box3) > 0:
                min_v = min(min_v, max(len(box1), len(box2), len(box3)) - min(len(box1), len(box2), len(box3)))
                find = True

    if find:
        print(f'#{tc} {min_v}')
    else:
        print(f'#{tc} {-1}')
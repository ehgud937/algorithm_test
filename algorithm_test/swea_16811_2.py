t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = -1
    min_v = 99999
    find = False

    for i in range(1, N-1):
        if arr[i] == arr[i-1]:
            continue
        for j in range(i+1, N):
            if arr[j] == arr[j-1]:
                continue
            current = 0
            box1 = arr[:i]
            box2 = arr[i:j]
            box3 = arr[j:]

            if len(box1) <= N//2 and len(box2) <= N//2 and len(box3) <= N//2:
                if len(box1) > 0 and len(box2) > 0 and len(box3) > 0:
                    current = max(len(box1), len(box2), len(box3)) - min(len(box1), len(box2), len(box3))
                    find = True
                    if current < min_v:
                        min_v = current


    if find:
        print(f'#{tc} {min_v}')
    else:
        print(f'#{tc} {-1}')
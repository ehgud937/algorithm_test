t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [0] * N

    for i in range(N):
        start, end = map(int, input().split())
        arr[i] = [start, end]

    arr.sort(key=lambda x:(x[1]))
    cnt = 0
    while arr:
        try:
            if arr[0][1] <= arr[1][0]:
                cnt += 1
                if len(arr) == 2:
                    if arr[0][1] <= arr[1][0]:
                        cnt += 1
                        break
                    else:
                        break
                else:
                    arr.pop(0)
            else:
                arr.pop(1)
        except:
            cnt += 1
            break
    print(f'#{tc} {cnt}')
t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    n = 0

    while True:
        if arr[0] == 0 or arr[1] == 0 or arr[2] == 0:
            n = -1
            break

        if arr[1] >= arr[2]:
            arr[1] -= 1
            n += 1
        elif arr[0] >= arr[1]:
            arr[0] -= 1
            n += 1
        else:
            break


    print(f'#{tc} {n}')
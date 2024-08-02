t = int(input())

for tc in range(1, t+1):
    total, a, b = map(int, input().split())

    arr = list(range(1, total + 1))
    start_a = 0
    end_a = (len(arr)-1)
    n_a = 0

    while start_a <= end_a:
        middle = (start_a + end_a)//2
        if arr[middle] == a:
            n_a += 1
            break
        elif arr[middle] > a:
            end_a = middle
            n_a += 1
        else:
            start_a = middle
            n_a += 1

    start_b = 0
    end_b = (len(arr)-1)
    n_b = 0
    while start_b <= end_b:
        middle = (start_b + end_b)//2
        if arr[middle] == b:
            n_b += 1
            break
        elif arr[middle] > b:
            end_b = middle
            n_b += 1
        else :
            start_b = middle
            n_b += 1

    if n_a > n_b:
        print(f'#{tc} B')
    elif n_a < n_b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
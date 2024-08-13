for _ in range(1, 11):
    tc = int(input())

    arr = list(map(int, input().split()))

    num = 1

    while True:
        if num == 6:
            num = 1

        current = arr.pop(0)
        current = current - num

        if current <= 0:
            arr.append(0)
            break

        arr.append(current)
        num += 1

    print(f'#{tc}', *arr)
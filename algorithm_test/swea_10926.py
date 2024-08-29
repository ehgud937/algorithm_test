t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input()))
    i = 0
    result = []
    while i < len(arr)-1:
        current = 0
        squre = [6, 5, 4, 3, 2, 1, 0]
        for j in range(i, i+7):
            if arr[j] == 1:
                current += (2**squre[j%7])
        result.append(current)
        i += 7
    print(f'#{tc}', *result)

t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    cnt = 0
    arr1.sort()

    for i in arr2:
        if i not in arr1:
            continue
        low = 0
        high = N-1
        lst = []

        while low <= high:
            mid = (low + high) // 2

            if arr1[mid] == i:
                break

            elif arr1[mid] > i:
                high = mid - 1
                lst.append(1)

            else:
                low = mid + 1
                lst.append(2)

        for j in range(len(lst) - 1):
            if lst[j] == lst[j + 1]:
                break
        else:
            cnt += 1

    print(f'#{tc} {cnt}')
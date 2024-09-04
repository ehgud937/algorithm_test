def q_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return q_sort(left) + middle + q_sort(right)

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = q_sort(arr)
    print(f'#{tc} {result[N//2]}')

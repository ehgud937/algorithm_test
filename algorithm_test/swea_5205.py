

def q_sort(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return q_sort(left, k)
    elif k < len(left) + len(middle):
        return pivot
    else:
        return q_sort(right, k - len(left) - len(middle))

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = q_sort(arr, N//2)
    print(f'#{tc} {sorted_arr}')
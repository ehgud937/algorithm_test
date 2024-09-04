def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    global cnt
    result = []
    i = j =0
    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans= merge_sort(arr)
    print(f'#{tc}', ans[N//2], cnt)
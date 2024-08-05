def sel_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)
    
a = [3, 4, 1, 2, 8, 5, 6, 13, 11]

sel_sort(a, len(a))
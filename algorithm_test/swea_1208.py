for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dump):
        max_num = 0
        min_num = 200
        max_idx = 0
        min_idx = 0
        
        for idx, num in enumerate(arr):
            if num > max_num:
                max_num = num
                max_idx = idx
               
            if num < min_num:
                min_num = num
                min_idx = idx
        
        arr[max_idx] -= 1
        arr[min_idx] += 1
    
    print(f'#{tc} {max(arr) - min(arr)}')

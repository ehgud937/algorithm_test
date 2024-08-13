t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int , input()))
    arr.sort()
    max_count = 0
    max_item = 0
    for i in range(n):
        cnt = 0
        cnt = arr.count(arr[i])
        if cnt >= max_count:
            max_count = cnt
            max_item = arr[i]
                
    print(f'#{tc} {max_item} {max_count}')

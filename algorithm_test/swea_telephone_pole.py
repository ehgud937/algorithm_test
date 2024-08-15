t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    cnt = 0

    for _ in range(n):
        line = list(map(int, input().split()))
        arr.append(line)
    
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                cnt += 1
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
    print(f'#{tc} {cnt}')
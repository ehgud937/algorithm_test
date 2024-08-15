t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = input().split()
    result = []

    if n % 2 == 0:
        for i in range(n//2):
            result.append(arr[i])
            result.append(arr[i + (n//2)])
    else:
        for i in range(n//2+1):
            result.append(arr[i])
        
            if i+(n//2+1) < n:
                result.append(arr[i + (n//2+1)])
         
    print(f'#{tc}', *result)
t = int(input())

for tc in range(1, t+1):
    arr = '/' + input() + '/'
    
    cnt = 0
    
    for i in range(len(arr)):
        if arr[i] == '(' and arr[i+1] != ')':
            cnt += 1
        elif arr[i] == ')' and arr[i-1] != '(' and arr[i-1] != '/':
            cnt += 1
        elif arr[i] == '(' and arr[i+1] == ')':
            cnt += 1
    
    print(f'#{tc} {cnt}')

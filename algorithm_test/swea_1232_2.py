def four_basic(n):
    if arr[n] == '+':
        return postord(left[n]) + postord(right[n])
    elif arr[n] == '-':
        return postord(left[n]) - postord(right[n])
    elif arr[n] == '*':
        return postord(left[n]) * postord(right[n])
    else:
        return postord(left[n]) / postord(right[n])

def postord(n):
    if arr[n]:
        if arr[n].isdecimal():
            return int(arr[n])
        else:
            return four_basic(n)
    else:
        return 0

for tc in range(1, 11):
    N = int(input())
    arr = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    
    for _ in range(N):
        tlst = input().split()
        arr[int(tlst[0])] = tlst[1]
        
        if len(tlst) > 2:
            left[int(tlst[0])] = int(tlst[2])
            right[int(tlst[0])] = int(tlst[3])
    
    ans = postord(1)

    print(f'#{tc} {int(ans)}')
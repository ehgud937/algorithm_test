t = int(input())

for tc in range(1, t+1):
    n = int(input())
    
    arr = [list(input()) for _ in range(n)]
    
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, -1, 1]
    result = 'NO'

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 'o':
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    current = 1
                    while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                            current += 1
                            ni = ni + di[k]
                            nj = nj + dj[k]
                    if current == 5:
                        result = 'YES'
    print(f'#{tc} {result}')


#  for num in range(1, 6):
#                         ni = i + (di[k] * num)
#                         nj = j + (dj[k] * num)
#                         if arr[ni][nj] == 'o' and 0 <= ni < n and 0 <= nj < n:
#                             current += 1


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 'no'
    for k in range(2, n+1):
        for i in range(n-k+1):
            for j in range(n-k+1):
                cnt = 0
                nemo = 0
                for p in range(i, i+k):
                    for l in range(j, j+k):
                        cnt += 1
                        if arr[p][l] == '#':
                            nemo += 1
                if cnt == nemo:
                    result = 'yes'
    print(f'#{tc} {result}')
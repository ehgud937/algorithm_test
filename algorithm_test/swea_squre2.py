t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    max_i, min_i = -1, n
    max_j, min_j = -1, n

    result = 'yes'

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                if i > max_i:
                    max_i = i
                if i < min_i:
                    min_i = i
                if j > max_j:
                    max_j = j
                if j < min_j:
                    min_j = j
    
    if max_i - min_i != max_j - min_j:
        result = 'no'

    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j + 1):
            if arr[i][j] != '#':
                result = 'no'
                break
    print(f'#{tc} {result}')
import math

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = [list(input()) for _ in range(n)]
    
    min_i, max_i = n, -1
    min_j, max_j = n, -1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                if i < min_i:
                    min_i = i
                if i > max_i:
                    max_i = i
                if j < min_j:
                    min_j = j
                if j > max_j:
                    max_j = j
    result = 'yes'

    if (max_i-min_i) != (max_j - min_j):
        result = 'no'

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if arr[i][j] != '#':
                result = 'no'
                

    print(f'#{tc} {result}')
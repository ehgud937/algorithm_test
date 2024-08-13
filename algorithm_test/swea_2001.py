t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    max_kill = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            current_kill = 0
            for k in range(i, i + m):
                for l in range(j, j + m):
                    current_kill += arr[k][l]
            if current_kill > max_kill:
                max_kill = current_kill
    
    print(f'#{tc} {max_kill}')
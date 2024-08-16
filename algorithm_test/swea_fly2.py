t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_kill = 0

    for i in range(n-k+1):
        for j in range(n-k+1):
            current_kill = 0
            for p in range(i, i+k):
                for l in range(j, j+k):
                    current_kill += arr[p][l]
            
            if current_kill > max_kill:
                max_kill = current_kill

    print(f'#{tc} {max_kill}')

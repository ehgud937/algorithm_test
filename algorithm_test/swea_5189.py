def per(n):
    global max_v

    if len(current) == n-1:
        now = 0
        # current = [1] + current + [1]
        col = [1] + current + [1]

        for i in range(0, len(col)-1):
            now += arr[col[i]-1][col[i+1]-1]


        if now < max_v:
            max_v = now

        return

    for i in range(2, n+1):
        if i in current:
            continue
        current.append(i)
        per(n)
        current.pop()

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    current = []
    visited = []
    max_v = 999999999
    per(N)
    print(f'#{tc} {max_v}')


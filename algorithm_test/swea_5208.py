def go(n, total):
    global min_v

    if total > min_v:
        return

    if n == N-1:
        min_v = total
        return

    k = arr[n]

    for i in range(1, k+1):
        if n+i < N:
            go(n+i, total + 1)

t = int(input())

for tc in range(1, t+1):
    N, *arr = map(int, input().split())
    min_v = 9999
    go(0, 0)
    print(f'#{tc} {min_v-1}')

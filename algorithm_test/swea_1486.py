t = int(input())

for tc in range(1, t+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = 999999

    for i in range(1 << N):
        current = 0
        for j in range(N):
            if i & (1 << j):
                current += arr[j]

        if current >= S and current < min_v:
            min_v =current
    print(f'#{tc} {min_v-S}')
t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())

    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        ai, bi = bi, ai

    max_v = 0

    for i in range(M-N+1):
        current = 0
        for j in range(N):
            current += ai[j] * bi[j+i]
        if current > max_v:
            max_v = current

    print(f'#{tc} {max_v}')
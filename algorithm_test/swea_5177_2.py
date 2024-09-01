t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    h = [0] * (N+1)
    last = 0

    for n in arr:
        last += 1
        h[last] = n

        c = last

        while c//2 and h[c] < h[c//2]:
            h[c], h[c//2] = h[c//2], h[c]
            c //= 2
        
    ans = 0
    c = last//2
    while c > 0:
        ans += h[c]
        c //= 2

    print(f'#{tc} {ans}')
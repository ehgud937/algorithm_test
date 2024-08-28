t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())

    lst = [0] * (n+1)

    for _ in range(m):
        idx, num = map(int, input().split())
        lst[idx] = num

    for i in range(len(lst)-1, 0, -1):
        if lst[i] == 0:
            if i * 2 <=n and i * 2 + 1 > n:
                lst[i] = lst[i*2]
            if i * 2 <= n and i * 2 + 1 <= n:
                lst[i] = lst[i*2] + lst[i*2+1]
    print(f'#{tc} {lst[k]}')
def dfs(n, fee):
    global total_fee
    if n > 12:
        if fee < total_fee:
            total_fee = fee
            return

    else:
        dfs(n+1, fee + (arr[n] * day))
        dfs(n+1, fee + month)
        dfs(n+3, fee + month_3)
        dfs(n+12, fee + year)

t = int(input())
for tc in range(1, t+1):
    day, month, month_3, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    total_fee = 99999999999
    dfs(1, 0)
    print(f'#{tc} {total_fee}')
def dfs(n, money):
    global min_v

    if money > min_v:
        return

    if n > 12:
        if money < min_v:
            min_v = money
        return

    dfs(n+1, money+(arr[n] * day))
    dfs(n+1, money+month)
    dfs(n+3, money+month_3)

t = int(input())

for tc in range(1, t+1):
    day, month, month_3, year = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    min_v = year
    dfs(1, 0)

    print(f'#{tc} {min_v}')
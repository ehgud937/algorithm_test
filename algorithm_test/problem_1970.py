t = int(input())

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, t+1):
    money = int(input())
    result = []

    for change in money_list:
        cnt = 0
        cnt += (money // change)
        result.append(cnt)
        money = money % change
    
    print(f'#{tc}')
    print(*result)
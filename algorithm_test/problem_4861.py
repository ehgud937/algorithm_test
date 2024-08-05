t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    str_list = [list(map(str, input())) for _ in range(n)]
    result = ''
    now_str = []
    for row in str_list:
        for i in range(len(row)-1, -1, -1):
            now_str.append(row[i])
        if row == now_str:
            result = now_str
        now_str = []

    for row in list(zip(*str_list)):
        for i in range(len(row) - 1, -1, -1):
            now_str.append(row[i])
        print(row, now_str)
        if list(row) == now_str:
            result = now_str
        now_str = []

    print(f'#{tc}', *result)
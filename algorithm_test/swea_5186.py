t = int(input())

for tc in range(1, t+1):
    n = float(input())
    result = ''
    while n != 0:
        n *= 2
        if n >= 1:
            result += '1'
            n -= 1
        else:
            result += '0'
            n = n
    if len(result) >= 13:
        result = 'overflow'
    print(f'#{tc} {result}')
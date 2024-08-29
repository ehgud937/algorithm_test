t = int(input())

for tc in range(1, t+1):
    d, a, b, fly = map(int, input().split())

    time = d / (a + b)

    print(f'#{tc} {time*fly}')
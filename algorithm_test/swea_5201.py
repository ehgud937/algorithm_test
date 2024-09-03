t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    express = list(map(int, input().split()))
    bus = list(map(int, input().split()))

    express.sort(reverse=True)
    bus.sort(reverse=True)
    result = 0

    while True:
        if not bus or not express:
            break
        if bus[0] >= express[0]:
            bus.pop(0)
            result += express.pop(0)
        else:
            express.pop(0)

    print(f'#{tc} {result}')
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = []

    for i in range(n):
        if i % 2 == 0:
            result.append(arr.pop())
        else:
            result.append(arr.pop(0))
    print(f'#{tc}', *result[:10])

    
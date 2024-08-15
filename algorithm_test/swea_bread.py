t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = 'Possible'

    for i in range(n):
        bungeoppang = (arr[i] // m) * k

        if bungeoppang < i+1:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')
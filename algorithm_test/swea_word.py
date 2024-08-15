t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(n)]
    arr.append([0] * (n + 1))

    cnt = 0

    for i in range(n+1):
        current = 0
        for j in range(n+1):
            if arr[i][j] == 1:
                current += 1
            else:
                if current == k:
                    cnt += 1
                    current = 0
                current = 0
    
    for i in range(n+1):
        current = 0
        for j in range(n+1):
            if arr[j][i] == 1:
                current += 1
            else:
                if current == k:
                    cnt += 1
                    current = 0
                current = 0
    print(f'#{tc} {cnt}')
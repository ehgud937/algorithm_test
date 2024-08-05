t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    for row in puzzle:
        current = 0
        for value in row:
            if value == 1:
                current += 1
            else:
                if current == k:
                    count += 1
                current = 0
        if current == k:
            count += 1

    for row in list(zip(*puzzle)):
        current = 0
        for value in row:
            if value == 1:
                current += 1
            else:
                if current == k:
                    count += 1
                current = 0
        if current == k:
            count += 1
    print(f'#{tc} {count}')
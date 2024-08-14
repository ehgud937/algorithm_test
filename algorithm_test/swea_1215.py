for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    max_cnt = 0
    
    for row in arr:
        for i in range(len(row)-n + 1):
            now = row[i : i + n]
            if now == now[::-1]:
                max_cnt += 1

    for row in list(zip(*arr)):
        for i in range(len(row)-n + 1):
            now = row[i : i + n]
            if now == now[::-1]:
                max_cnt += 1
    print(f'#{tc} {max_cnt}')
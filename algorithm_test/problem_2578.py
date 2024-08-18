arr = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
for _ in range(5):
    number = list(map(int, input().split()))

    for k in number:
        cnt += 1
        tmp = 0
        for i in range(5):
            for j in range(5):
                if arr[i][j] == k:
                    arr[i][j] = -1
        
        for i in arr:
            if sum(i) == -5:
                tmp += 1
        
        for i in range(5):
            now = 0
            for j in range(5):
                now += arr[j][i]
            if now == -5:
                tmp += 1
        
        cross = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    cross += arr[i][j]
        if cross == -5:
            tmp += 1

        cross2 = 0
        for i in range(5):
            for j in range(5):
                if 4-i == j:
                    cross2 += arr[i][j]
        if cross2 == -5:
            tmp += 1

        if tmp >= 3:
            break
    
    if tmp >= 3:
        break

print(cnt)
        
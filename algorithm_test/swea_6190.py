t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_cnt = -1

    for i in range(n-1):
        for j in range(i+1, n):
            cnt = str(arr[i] * arr[j])
            current = 0
            for k in range(len(cnt)-1):
                if int(cnt[k]) > int(cnt[k+1]):
                    current = 1
            if current == 0:
                if int(cnt) > max_cnt:
                    max_cnt = int(cnt)

    print(f'#{tc} {max_cnt}')


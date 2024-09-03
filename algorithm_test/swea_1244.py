def per(n, k):
    global max_v
    if n == k or n == len(no_idea):
        cnt = ''
        for i in no_idea:
            cnt += i
        if int(cnt) > max_v:
            max_v = int(cnt)
        return

    for i in range(len(no_idea)):
        for j in range(i+1, len(no_idea)):
            no_idea[i], no_idea[j] = no_idea[j], no_idea[i]
            per(n+1, k)
            no_idea[i], no_idea[j] = no_idea[j], no_idea[i]


t = int(input())

for tc in range(1, t+1):
    arr, k = input().split()
    no_idea = list(arr)

    k = int(k)
    current = []
    max_v = 0
    per(0, k)

    print(f'#{tc} {max_v}')
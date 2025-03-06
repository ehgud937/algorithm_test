from collections import deque
tc = int(input())

for _ in range(tc):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    q = deque()
    
    for idx, num in enumerate(arr):
        q.append((num, idx))

    while True:
        now_max = max(q)
        now_print = q.popleft()
        
        if now_max[0] == now_print[0]:
            cnt += 1
            if now_print[1] == M:
                break
        else:
            q.append(now_print)
    print(cnt)
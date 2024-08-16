t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    busstop = [0] * p
 
    for i in range(p):
        line = int(input())
        cnt = 0
        for bus in arr:
            if bus[0] <= line <= bus[1]:
                cnt += 1
        busstop[i] = cnt
    
    
    print(f'#{tc}', *busstop)

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_carrot = 0
    max_idx = 0
    
    for idx, carrot in enumerate(arr):
        if carrot > max_carrot:
            max_carrot = carrot
            max_idx = (idx+1)
    
    print(f'#{tc} {max_idx} {max_carrot}')
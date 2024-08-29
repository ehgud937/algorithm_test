t = int(input())

for tc in range(1, t+1):
    box1, box2, box3 = map(int, input().split())
    cnt = 0
    if box1 < box2 and box2 < box3:
        cnt = 0
    else:
        while True:
            if box1 == 0 or box2 == 0 or box3 == 0:
                cnt = -1
                break
            elif box2 >= box3:
                box2 -= 1
                cnt += 1
            elif box1 >= box2:
                box1 -= 1
                cnt += 1
            elif box1 < box2 and box2 < box3:
                break



    print(f'#{tc} {cnt}')
t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    play1 = []
    play2 = []

    i = 0
    result = 0
    result1 = 0
    result2 = 0

    while True:
        if i > 11:
            result = 0
            break

        play1.append(arr[i])
        i += 1
        if len(play1) >= 3:
            lst = [0] * 10

            for k in play1:
                lst[k] += 1

            for j in lst:
                if j >= 3:
                    result1 = 1

            for p in range(0, len(lst) - 2):
                if lst[p] >= 1 and lst[p+1] >= 1 and lst[p+2] >= 1:
                    result1 = 1
        if result1 == 1:
            result = 1
            break

        play2.append(arr[i])
        i += 1

        if len(play2) >= 3:
            lst = [0] * 10

            for k in play2:
                lst[k] += 1

            for j in lst:
                if j >= 3:
                    result2 = 1

            for p in range(0, len(lst) - 2):
                if lst[p] >= 1 and lst[p + 1] >= 1 and lst[p + 2] >= 1:
                    result2 = 1
        if result2 == 1:
            result = 2
            break




    print(f'#{tc} {result}')
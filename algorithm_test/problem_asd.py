t = int(input())

for tc in range(1, t+1):
    num = input()
    card = [0] * len(num)
    for i in range(len(num)):
        card[i] = int(num[i])

    counts = [0] * 10
    triple = 0
    runs = 0

    for num in card:
        counts[num] += 1

    for i in range(len(counts)):
        if counts[i] >= 3:
            if counts[i] == 6:
                triple += 2
                counts[i] -= 6
            else:
                triple += 1
                counts[i] -= 3

    for i in range(len(counts) - 2):
        while counts[i] > 0 and counts[i + 1] > 0 and counts[i + 2] > 0:
            runs += 1
            counts[i] -= 1
            counts[i + 1] -= 1
            counts[i + 2] -= 1

    if runs + triple == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
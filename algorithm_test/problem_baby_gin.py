card = [1, 2, 3, 4, 5, 6]
counts = [0] * 10
triple = 0
run = 0


for num in card:
    counts[num] += 1



for i in range(len(counts)):
    if counts[i] >= 3:
        triple += 1
        counts[i] -= 3



for i in range(len(counts) - 2):
    while counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
        run += 1
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1


if run + triple == 2:
    print('Baby Gin')
else:
    print('lose')

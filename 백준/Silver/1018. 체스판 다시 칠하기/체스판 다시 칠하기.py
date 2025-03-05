N, M = map(int, input().split())
arr = [input() for _ in range(N)]

min_repaint = 999999

for x in range(N - 7):
    for y in range(M - 7):
        W_first = 0
        B_first = 0

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:  
                    if arr[x + i][y + j] != 'W':
                        W_first += 1
                    if arr[x + i][y + j] != 'B':
                        B_first += 1
                else: 
                    if arr[x + i][y + j] != 'B':
                        W_first += 1
                    if arr[x + i][y + j] != 'W':
                        B_first += 1

        min_repaint = min(min_repaint, W_first, B_first)

print(min_repaint)

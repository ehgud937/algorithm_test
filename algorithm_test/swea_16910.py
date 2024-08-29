t = int(input())

for tc in range(1, t+1):
    n = int(input())

    result = 0
    for i in range(0, 2*n+1):
        for j in range(0, 2*n+1):
            if (i-n)**2 + (j-n)**2 <= (n**2):
                result += 1
    print(f'#{tc} {result}')
t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        a, b = b, a
    
    max_sum = 0

    for i in range(m - n + 1):
        current_sum = 0
        for j in range(n):
            current_sum += a[j] * b[i + j]
        if current_sum > max_sum:
            max_sum = current_sum
    
    print(f'#{tc} {max_sum}')
def per_sum(n, k, total):
    global result

    if total > k:
        return

    if n > N-1:
        return

    if total == k:
        now = ''
        for i in visited:
            now += str(i)
        result.add(now)

        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            per_sum(n+1, k, total + arr[i])
            visited[i] = 0

t = int(input())

for tc in range(1, t+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * N
    result = set()
    per_sum(0, K, 0)
    print(f'#{tc} {len(result)}')

t = int(input())

for tc in range(1, t+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(1 << N):
        current = 0
        now = []
        for j in range(N):
            if i & (1 << j):
                current += arr[j]
                now.append(arr[j])
        if current == K:
            cnt += 1

    print(f'#{tc} {cnt}')

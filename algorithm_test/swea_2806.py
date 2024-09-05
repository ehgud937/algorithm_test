def check(n):
    for col in range(n):
        if visited[n] == visited[col]:
            return True
        if abs(visited[n] - visited[col]) == abs(n - col):
            return True

    return False


def n_queen(n):
    global cnt

    if n == N:
        cnt += 1
        return

    for col in range(N):
        visited[n] = col
        if check(n):
            continue

        n_queen(n+1)

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    visited = [0] * N
    cnt = 0
    n_queen(0)

    print(f'#{tc} {cnt}')


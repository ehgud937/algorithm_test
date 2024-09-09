def dfs(n):
    global min_v

    if n == N:
        if sum(visited) == N//2:
            cook1 = []
            cook2 = []
            for i in range(N):
                if visited[i] == 1:
                    cook1.append(i)
                else:
                    cook2.append(i)
            synergy1 = mix(cook1)
            synergy2 = mix(cook2)

            min_v = min(min_v, abs(synergy1-synergy2))
        return

    visited[n] = 1
    dfs(n+1)
    visited[n] = 0
    dfs(n+1)

def mix(lst):
    cnt = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            cnt += (arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]])

    return cnt

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    min_v = 999999
    dfs(0)

    print(f'#{tc} {min_v}')
def dfs(k):
    arr[k] = -2

    for i in range(N):
        if arr[i] == k:
            dfs(i)

N = int(input())
arr = list(map(int, input().split()))
k = int(input())

dfs(k)

ans = 0

for i in range(N):
    if arr[i] != -2 i not in arr:
        ans += 1

print(ans)
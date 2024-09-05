def perfect_job(n, total):
    global max_v

    if total * 100 <= max_v:
        return

    if n == N:
        max_v = total * 100

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            perfect_job(n+1, total * (arr[n][i] / 100))
            visited[i] = 0

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    visited = [0] * N
    perfect_job(0, 1)
    print(f'#{tc}{max_v : .6f}')
#
# def perfect_job(n, total):
#     global max_v
#
#     if total <= max_v:
#         return
#
#     if n == N:
#         max_v = total
#         # if total > max_v:
#         #     max_v = round(total,6)
#         #     return
#
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             perfect_job(n+1, total * (arr[n][i]/100))
#             visited[i] = 0
#
# t = int(input())
#
# for tc in range(1, t+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_v = 0
#     visited = [0] * N
#     perfect_job(0, 1)
#     print(f'#{tc} {max_v/10000}')


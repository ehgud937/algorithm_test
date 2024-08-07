t = int(input())

def DFS(s, V, G):              # s 시작정점, V 정점개수(마지막정점)
    visited = [0] * (V+1)   # 방문한 정점을 표시
    stack = []              # 스택 생성

    visited[s] = 1          # 시작정점 방문표시
    v = s
    while True:
        for w in dfs_list[v]:    # v에 인접하고, 방문 안 한 w가 있으면
            if visited[w] == 0:
                stack.append(v)   # push(v) 현재 정점을 push하고
                v = w
                if v == G:
                    return 1

                visited[w] = 1    # w에 방문 표시
                break             # fow w에 대한 break, v부터 다시 탐색
        else:                     # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack:             # 이전 갈림길을 스택에서 꺼내서....
                v = stack.pop()
            else:       # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색종료
                return 0   # while True에 대한 break

for tc in range(1, t+1):
    V, E = map(int, input().split())
    dfs_list = [[] for _ in range(V+1)]

    for _ in range(E):
        v1 , v2 = map(int, input().split())
        dfs_list[v1].append(v2)
    S, G = map(int, input().split())


    print(f'#{tc} {DFS(S, V, G)}')

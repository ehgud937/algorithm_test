t = int(input())

def DFS(s, V):              # s 시작정점, V 정점개수(마지막정점)
    visited = [0] * (V+1)   # 방문한 정점을 표시
    stack = []              # 스택 생성
    print(s)
    visited[s] = 1          # 시작정점 방문표시
    v = s
    while True:
        for w in dfs_list[v]:    # v에 인접하고, 방문 안 한 w가 있으면
            if visited[w] == 0:
                stack.append(v)   # push(v) 현재 정점을 push하고
                v = w             # w에 방문
                print(v)
                visited[w] = 1    # w에 방문 표시
                break             # fow w에 대한 break, v부터 다시 탐색
        else:                     # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack:             # 이전 갈림길을 스택에서 꺼내서....
                v = stack.pop()
            else:       # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색종료
                break   # while True에 대한 break

for tc in range(1, t+1):
    # V는 마지막 정점 번호, e는 간선의 개수
    V, e = map(int, input().split())
    arr = list(map(int, input().split()))
    dfs_list = [[] for _ in range(v+1)]

    for i in range(e):
        v1, v2 = arr[i*2], arr[i*2+1]
        dfs_list[v1].append(v2)
        dfs_list[v2].append(v1)
    DFS(1, V)

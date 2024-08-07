v = int(input())
e = int(input())
cnt = 0

def DFS(s, v):
    global cnt
    visited = [0] * (v+1)
    stack = []
    visited[s] = 1
    visit = s

    while True:
        for w in computer_list[visit]:
            if visited[w] == 0:
                stack.append(visit)
                visit = w
                visited[w] = 1
                cnt += 1
                break
        else:
            if stack:
                visit = stack.pop()
            else:
                break






computer_list = [[] for i in range(v+1)]
for _ in range(e):
    v1, v2 = map(int, input().split())

    computer_list[v1].append(v2)
    computer_list[v2].append(v1)

DFS(1, v)
print(cnt)

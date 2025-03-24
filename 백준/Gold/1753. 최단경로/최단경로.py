import sys
import heapq

input = sys.stdin.readline

INF = int(9999999999999)

V, E = map(int, input().split())
K = int(input())

adj = [[] for _ in range(V+1)]

distance = [INF] * (V+1)
distance[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

q = []
heapq.heappush(q, (0, K))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for next_node, weight in adj[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

for i in range(1, V+1):
    if distance[i] == int(9999999999999):
        print('INF')

    else:
        print(distance[i])
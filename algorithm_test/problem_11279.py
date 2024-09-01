import heapq
import sys
input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    n = int(input())

    if n:
        heapq.heappush(h, -n)
    else:
        if n == 0 and not h:
            print(0)
        else:
            print(-heapq.heappop(h))
    
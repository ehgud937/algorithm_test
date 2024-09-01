import heapq

N = int(input())
dasom = int(input())
h = []

for i in range(N-1):
    K = int(input())

    if K >= dasom:
        heapq.heappush(h, -K)

buy_vote = 0

while h:
    vote = -heapq.heappop(h)
    if dasom > vote:
        break
    dasom += 1
    buy_vote += 1
    heapq.heappush(h, -(vote -1))
print(buy_vote)
    
N = int(input())

arr = []

for _ in range(N):
    i, j = map(int, input().split())
    arr.append((i, j))

arr.sort(key= lambda x:(x[0], x[1]))

for i,j in arr:
    print(i, j)
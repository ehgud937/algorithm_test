import itertools

n = int(input())

arr = list(itertools.permutations(range(1,n+1)))

for i in arr:
    print(*i)
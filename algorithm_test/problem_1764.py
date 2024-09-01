N, M = map(int, input().split())

hear = set()
see = set()

for _ in range(N):
    hear.add(input())

for _ in range(M):
    see.add(input())    

result = []
for name in hear:
    if name in see:
        result.append(name)
        
result.sort()
print(len(result))
for i in result:
    print(i)
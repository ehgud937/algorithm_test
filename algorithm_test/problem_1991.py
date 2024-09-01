def preord(n):
    if n == '.':
        return
    
    print(n, end='')
    preord(tree[n][0])
    preord(tree[n][1])

def inord(n):
    if n == '.':
        return
    inord(tree[n][0])
    print(n, end='')
    inord(tree[n][1])

def postord(n):
    if n == '.':
        return 
    postord(tree[n][0])
    postord(tree[n][1])
    print(n, end='')  

N = int(input())

tree = {}

for _ in range(N):
    tlst = input().split()
    tree[tlst[0]] = (tlst[1], tlst[2])

preord('A')
print()
inord('A')
print()
postord('A')
print()
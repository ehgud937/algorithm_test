import sys

n = int(sys.stdin.readline().lstrip())

a = list(map(int, sys.stdin.readline().lstrip().split()))

s = [0] * n

for i in range(n):
    for j in range(i + 1, n):
        
        if not a[i] % a[j] : s[i], s[j] = s[i] - 1, s[j] + 1
        
        elif not a[j] % a[i] : s[i] , s[j] = s[i] + 1, s[j] - 1
    
    sys.stdout.write(f'{s[i]}')
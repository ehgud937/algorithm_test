import sys

p = int(sys.stdin.readline())
n = int(sys.stdin.readline())
text = sys.stdin.readline()

word = 'IOI' + ('OI' * (p-1))
result = 0

for i in range(n - len(word) + 1):
    if text[i : i + len(word)] == word:
        result += 1
print(result)

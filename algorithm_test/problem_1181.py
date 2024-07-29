n = int(input())
words = [0] * n
for i in range(n):
    words[i] = input()
words = list(set(words))
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)
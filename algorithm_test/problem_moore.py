text = 'I love vv water'
word = 'water'
n = len(text)
m = len(word)
i = 0
for i in range(i, n-m+1):
    if text[i+m-1] != word[-1]:
        if text[i+m-1] not in word:
            i += m
            print(i)
    elif text[i:i+m] == word:
        print('yes')
        break
else:
    print('no')


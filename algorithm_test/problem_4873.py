t = int(input())

for tc in range(1, t+1):
    words = list(input())
    result = []
    for word in words:
        if word not in result:
            result.append(word)
        elif word in result:
            if result[-1] != word:
                result.append(word)
            elif result[-1] == word:
                result.pop()
    print(f'#{tc} {len(result)}')
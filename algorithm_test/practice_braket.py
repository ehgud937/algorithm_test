
def is_braket(s):
    stack = []
    pair = {')': '(',
            ']': '[',
            '}': '{'}
    for i in range(len(s)):
        if s[i] in pair.values():
            stack.append(s[i])
        elif s[i] in pair.keys():
            if stack == [] or pair[s[i]] != stack.pop():
                return 0
        else:
            continue
    if stack == []:
        return 1
    else:
        return 0
t = int(input())

for tc in range(1, t+1):
    s = input()
    print(f'#{tc} {is_braket(s)}')
def calculation(output):
    stack = []
    try:
        for i in range(len(output)):
            if output[i].isnumeric():
                stack.append(int(output[i]))

            else:
                if output[i] == '+':
                    a = stack.pop()
                    b = stack.pop()
                    c = b + a
                    stack.append(c)
                elif output[i] == '-':
                    a = stack.pop()
                    b = stack.pop()
                    c = b - a
                    stack.append(c)
                elif output[i] == '*':
                    a = stack.pop()
                    b = stack.pop()
                    c = b * a
                    stack.append(c)
                elif output[i] == '/':
                    a = stack.pop()
                    b = stack.pop()
                    c = b / a
                    stack.append(c)

        if len(stack) > 1:
            return 'error'
        else:
            return int(stack.pop())

    except:
        return 'error'

t = int(input())

for tc in range(1, t+1):
    output = list(map(str, input().split()))
    print(f'#{tc} {calculation(output)}')
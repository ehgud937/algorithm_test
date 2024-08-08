def to_rpn(notation):
    level = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    for i in range(len(notation)):
        if notation[i].isnumeric():
            output.append(notation[i])
        else:
            while stack and level[notation[i]] <= level[stack[-1]]:
                output.append(stack.pop())
            stack.append(notation[i])

    while stack:
        output.append(stack.pop())

    return output

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

for tc in range(1, 11):
    n = int(input())
    notation = input()
    output = to_rpn(notation)
    print(f'#{tc} {calculation(output)}')
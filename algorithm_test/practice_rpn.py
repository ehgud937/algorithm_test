

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
                c = b // a
                stack.append(c)
    return stack.pop()


output = to_rpn(notation)

print(calculation(output))
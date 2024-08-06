def my_push(item):
    global top
    top += 1
    if top == size:
        print('OverFlow')
    else:
        stack[top] = item

def my_pop():
    global top
    if top == -1:
        print('UnderFlow')
        return 0
    else:
        top -= 1
        return stack[top + 1]


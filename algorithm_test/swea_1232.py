def postorder(node):
    if node == 0:
        return

    if isinstance(top[node], int):
        return top[node]

    a = postorder(left[node])
    b = postorder(right[node])

    return four_basic(a, b, top[node])


def four_basic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    else:
        return a // b

for tc in range(1, 11):
    n = int(input())

    left = [0] * (n + 1)
    right = [0] * (n + 1)
    top = [0] * (n + 1)

    for _ in range(n):
        node, *other = input().split()
        node = int(node)
        if len(other) == 3:
            left[node] = int(other[1])
            right[node] = int(other[2])
            top[node] = other[0]
        else:
            top[node] = int(other[0])

    result = postorder(1)
    print(f'#{tc} {result}')

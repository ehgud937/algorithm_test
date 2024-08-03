t = int(input())

for tc in range(1, t+1):
    braket = input()
    stack = []
    result = 0

    for i in range(len(braket)):
        if braket[i] == '(':
            stack.append(braket[i])
        else:
            if braket[i-1] == '(':
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
    print(f'#{tc} {result}')
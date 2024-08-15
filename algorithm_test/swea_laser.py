t = int(input())

for tc in range(1, t+1):
    laser = input() + '/'
    stack = []
    cnt = 0

    for i in range(len(laser)-1):
        if laser[i] == '(' and laser[i+1] == '(':
            stack.append('(')
        elif laser[i] == '(' and laser[i+1] == ')':
            cnt += len(stack)
        elif laser[i] == ')' and laser[i-1] != '(':
            stack.pop()
            cnt += 1
    print(f'#{tc} {cnt}')  
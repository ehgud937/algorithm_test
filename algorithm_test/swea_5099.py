from collections import deque

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    my_list = deque()

    for idx, che in enumerate(arr):
        my_list.append([che,idx])

    i = n
    q = deque()

    for _ in range(n):
        q.append(my_list.popleft())

    while len(q) > 1:
        pizza = q.popleft()

        if pizza[0] // 2 != 0:
            pizza[0] = pizza[0] // 2
            q.append(pizza)

        elif pizza[0] // 2 == 0 and len(my_list) >= 1:
            q.append(my_list.popleft())

    print(f'#{tc} {q[0][1]+1}')


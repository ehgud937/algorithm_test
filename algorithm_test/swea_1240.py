dic = {'0001101' : 0,
       '0011001' : 1,
       '0010011' : 2,
       '0111101' : 3,
       '0100011' : 4,
       '0110001' : 5,
       '0101111' : 6,
       '0111011' : 7,
       '0110111' : 8,
       '0001011' : 9}

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)    ]
    password = []
    for row in arr:
        for j in range(0, m-55):
            candidate1 = row[j : j + 56]
            candidate2 = row[j+56 :]
            if 1 in candidate1 and 1 not in candidate2:
                password = candidate1
                break
    result = []
    for i in range(0, len(password), 7):
        current = ''
        for j in range(i, i+7):
            current += str(password[j])

        result.append(current)

    answer = []

    for item in result:
        answer.append(dic[item])

    answer = [0] + answer

    odd = 0
    even = 0

    for i in range(len(answer)):
        if i % 2 == 0:
            even += answer[i]
        else:
            odd += answer[i]

    if ((odd*3) + even) % 10 == 0:
        print(f'#{tc} {sum(answer)}')
    else:
        print(f'#{tc} 0')
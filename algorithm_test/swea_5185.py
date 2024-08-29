binary = {}
hexade = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(0, 10):
    binary[str(i)] = i

for i in range(len(hexade)):
    binary[hexade[i]] = i + 10

t = int(input())

for tc in range(1, t+1):
    n, hexa = input().split()
    result = []


    for i in hexa:
        num = binary[i]
        current = ''
        while len(current) < 4:
            current += str(num%2)
            num = num//2
        result.append(current[::-1])
    answer = ''
    for i in result:
        answer += i
    print(f'#{tc} {answer}')



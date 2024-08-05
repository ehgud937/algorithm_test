t = int(input())

for tc in range(1, t+1):
    str1 = input()
    str2 = list(input())

    for i in range(len(str2) - len(str1) + 1):
        word = ''
        result = 0
        for j in range(i, i + len(str1)):
            word += str2[j]

        if word == str1:
            result = 1
            print(f'#{tc} {result}')
            break
    if result != 1:
        print(f'#{tc} {result}')
t = int(input())

for tc in range(1, t+1):
    str1 = list(input())
    str2 = list(input())
    result = 0
    for i in range(len(str2) - len(str1) + 1):
        if str2[i : i + len(str1)] == str1:
            result = 1
    print(f'#{tc} {result}')
t = int(input())

for tc in range(1, t+1):
    my_str, sub_str = map(str, input().split())
    n = 0
    i = 0

    while i <= len(my_str) - len(sub_str):
        if my_str[i:i + len(sub_str)] == sub_str:
            n += 1
            i += len(sub_str)
        else:
            i += 1

    result = (len(my_str) - (n * len(sub_str))) + n
    print(f'#{tc} {result}')
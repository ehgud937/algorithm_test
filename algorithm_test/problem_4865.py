t = int(input())

for tc in range(1, t+1):
    str1 = list(input())
    str2 = list(input())
    my_dict = {}
    for my_str in str1:
        my_dict[my_str] = 0
        for i in range(len(str2)):
            if my_str == str2[i]:
                my_dict[my_str] += 1
    max_cnt = 0
    for value in my_dict.values():
        if value > max_cnt:
            max_cnt = value
    print(f'#{tc} {max_cnt}')
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    my_list = list(map(int, input().split()))
    new_list = []

    while my_list:
        max_num = 0
        min_num = 999999
        max_i = 0
        min_i = 0
        for i in range(len(my_list)):
            if my_list[i] > max_num:
                max_num = my_list[i]
                max_i = i
        new_list.append(my_list[max_i])
        my_list.pop(max_i)

        for j in range(len(my_list)):
            if my_list[j] < min_num:
                min_num = my_list[j]
                min_i = j

        new_list.append(my_list[min_i])
        my_list.pop(min_i)


    print(f'#{tc} {" ".join(map(str, new_list[0:10]))}')
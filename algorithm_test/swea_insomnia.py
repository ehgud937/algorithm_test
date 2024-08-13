t = int(input())

for tc in range(1, t+1):
    n = int(input())
    my_list = []
    
    i = 1
    result = 0
    while len(my_list) < 10:
        number = n * i
        str_n = str(number)

        for char in str_n:
            my_list.append(char)

        my_list = list(set(my_list))
        i += 1
        result = number
    
    print(f'#{tc} {result}')


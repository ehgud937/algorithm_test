t = int(input())

for tc in range(1, t+1):
    n = int(input())
    my_list = list(map(int, input().split()))


    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    print(f'#{tc} {" ".join(map(str, my_list))}')


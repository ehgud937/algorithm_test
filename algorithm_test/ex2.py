t = int(input())
my_list = list(map(int, input().split()))

max_num = 0
for i in range(len(my_list)):
    count = 0
    for j in range(len(my_list)):
        if my_list[i] > my_list[j]:
            count += 1
    if max_num < count:
        max_num = count
print(max_num)
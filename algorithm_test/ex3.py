n = int(input())

my_list = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)
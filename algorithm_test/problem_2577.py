a = int(input())
b = int(input())
c = int(input())

numbers = a * b * c
str_num = str(numbers)
num_list = []

for i in str_num :
    num_list.append(i)

for j in range(10) :
    print(num_list.count(str(j)))
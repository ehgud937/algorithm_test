my_list = [0, 4, 1, 3, 1, 2, 4, 1]
k = 5

new_list = [0] * k
temp = [0] * len(my_list)
for num in my_list:
    new_list[num] += 1

for i in range(1, k):
    new_list[i] += new_list[i-1]
print(new_list)


for j in range(len(temp)-1, -1, -1):
    new_list[my_list[j]] -= 1
    idx = new_list[my_list[j]]
    print(idx)
    temp[new_list[my_list[j]]] = my_list[j]

print(temp)
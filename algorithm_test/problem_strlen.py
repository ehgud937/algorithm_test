# a = ['a', 'b', 'c', 'W0']
# i = 0
# num = 0
# while a[i] != 'W0':
#     if a[i] != 'W0':
#         num += 1
#     i += 1
# print(num)

s = 'Reverse this strings'

n = 0
reverse_list = [0] * len(s)
reverse_list2 = [0] * len(s)
for i in range(len(s)-1, -1, -1):
    reverse_list[n] = s[i]
    n += 1
print(('').join(reverse_list))
print(*reverse_list)

for i in range(len(s)//2):
    reverse_list2[i], reverse_list2[len(s)-i-1] = reverse_list2[len(s)-i-1], reverse_list2[i]
print(reverse_list2)



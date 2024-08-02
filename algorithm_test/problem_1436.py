t = int(input())

find = 0
result = 0
find_666 = 0
i = 1

while t > find_666:
    if '666' in str(i):
        find_666 += 1
        result = i
    i += 1
print(result)
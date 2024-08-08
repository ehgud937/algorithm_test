n = int(input())
num = 0
max_cnt = 0
result = []

for num in range(0, n+1):
    num_list = []
    num_list.append(n)
    num_list.append(num)
    i, cnt = 2, 2
    while True:
        num_list.append( num_list[i-2] - num_list[i-1])
        num = num_list[i]
        
        if num < 0:
            num_list.pop()
            break
        else:
            i += 1
            cnt += 1
    
    if cnt > max_cnt:
        max_cnt = cnt
        result = num_list


print(len(result))
print(*result)
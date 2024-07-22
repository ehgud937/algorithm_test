t = int(input())

for i in range(t) :
    str_list = []
    num, word = map(str,input().split())
    num = int(num)
    for j in word :
        str_list.append(j*num)
    print(''.join(str_list))
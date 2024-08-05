t = int(input())
list1 = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for _ in range(t):

    tc, length = map(str, input().split())

    num_list = list(map(str, input().split()))

    for i in range(len(list1)):
        for j in range(int(length)):
            if num_list[j] == list1[i]:
                num_list[j] = list2[i]

    for i in range(len(num_list)-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]


    for i in range(len(list1)):
        for j in range(int(length)):
            if num_list[j] == list2[i]:
                num_list[j] = list1[i]
    print(f'{tc}')
    print(*num_list)
# arr1 = [0] * 3
#
# arr2 = [[0] * 3 for _ in range(2)]

# for i in range(len(arr2)):
#     print(arr2[i])
#
#
# for i in range(len(arr2)):
#     print(*arr2[i])

# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end= ' ')
#     print()

# arr = [[1, 2, 3], [4, 5, 6]]
#
#
# max_v = 0
# for i in range(len(arr)):
#     s = 0
#     for j in range(len(arr[0])):
#         s += arr[i][j]
#     if s > max_v:
#         max_v = s
# print((max_v))
#
#
#
# max_v2 = 0
# for i in range(len(arr[0])):
#     s = 0
#     for j in range(len(arr)):
#         s += arr[j][i]
#     if s > max_v2:
#         max_v2 = s
# print((max_v2))

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

max_v = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        s = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < len(arr) and 0 <= nj < len(arr):
                s += arr[ni][nj]

        s += arr[i][j]

        if s > max_v:
            max_v = s
print(max_v)


arr2 = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]


# arr2 = [[1] * 5 for _ in range(5)]

max_v2 = 0
for i in range(len(arr2)):
    for j in range(len(arr2)):
        s = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < len(arr2) and 0 <= nj < len(arr2):
                s += abs(arr2[i][j] - arr2[ni][nj])
        if max_v2 < s:
            max_v2 = s
print(max_v2)

arr = [1, 3, 5, 7, 9]
n =len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j],end = ' ')
        print()
    # print()
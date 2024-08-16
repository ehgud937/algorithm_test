tc = int(input())

n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

arr1 = arr[0 : (n//2 + 1)]
arr1 = arr1[::-1]

arr2 = arr[(n//2 + 1):]

cnt = 0

for i in range(len(arr1)):
    for j in range(i, len(arr)-i):
        cnt += arr1[i][j]

for i in range(len(arr2)):
    for j in range(i+1, len(arr)-(i+1)):
        cnt += arr2[i][j]
        
print(f'#{tc} {cnt}')

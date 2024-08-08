t = int(input())
warehouse = []

for _ in range(t):
    pillar = list(map(int, input().split()))
    warehouse.append(pillar)

warehouse.sort()

max_hieght = 0
idx = 0
idx_2 = 0
for item in warehouse:
    if item[1] > max_hieght:
        max_hieght = item[1]
        idx = idx_2
        idx_2 += 1
    else:
        idx_2 += 1

height = warehouse[0][1]

result = warehouse[idx][1] * 1

for i in range(idx):
    if height < warehouse[i+1][1]:
        result += height * (warehouse[i+1][0] - warehouse[i][0])
        height = warehouse[i+1][1]
    
    else:
        result += height * (warehouse[i+1][0] - warehouse[i][0])

height = warehouse[-1][1]

for i in range(len(warehouse)-1, idx, -1):
    if height < warehouse[i-1][1]:
        result += height * (warehouse[i][0] - warehouse[i-1][0])
        height = warehouse[i-1][1]
    else:
        result += height * (warehouse[i][0] - warehouse[i-1][0])

print(result)
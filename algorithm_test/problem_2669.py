square_list = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, x2, y1, y2 = map(int, input().split())

    for i in range(x1, y1):
        for j in range(x2, y2):
            square_list[i][j] = 1
            
result = 0
for row in square_list:
    result += sum(row)
print(result)
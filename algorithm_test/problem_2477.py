n = int(input())
line = []
garo = []
sero = []

for _ in range(6):
    direction, length = map(int, input().split())
    line.append([direction,length])
    if direction == 1 or direction == 2:
        garo.append(length)
    else:
        sero.append(length)

max_width = max(garo)
max_height = max(sero)

max_width_idx = 0
max_height_idx = 0

for i in range(len(line)):
    if line[i][1] == max_width and (line[i][0] == 1 or line[i][0] == 2):
        max_width_idx = i
    if line[i][1] == max_height and (line[i][0] == 3 or line[i][0] == 4):
        max_height_idx = i

min_width = line[(max_width_idx+3) % 6][1]
min_height = line[(max_height_idx + 3) % 6][1]

result = (max_width * max_height) - (min_height * min_width)

print(result * n)
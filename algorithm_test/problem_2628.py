n, m = map(int,input().split())

t = int(input())

sero = [0, m]
garo = [0, n]

for _ in range(t):
    direction, num = map(int, input().split())
    if direction == 0:
        sero.append(num)
    else:
        garo.append(num)

sero.sort()
garo.sort()

max_garo = max(garo[i+1] - garo[i] for i in range(len(garo)-1))
max_sero = max(sero[i+1] - sero[i] for i in range(len(sero)-1))

print(max_garo * max_sero)
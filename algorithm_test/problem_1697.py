a, b = map(int, input().split())
result = 0
while a != b:
    if a < b:
        if abs(b - (a*2)) < abs(b - (a+1)):
            a *= 2
            result += 1
        else:
            a += 1
            result += 1
    else:
        if abs((a*2) - b) > abs((a-1) - b):
            a -= 1
            result += 1
print(result-1)
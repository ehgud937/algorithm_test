num = int(input())

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
number = str(fac(num))

result = 0

for i in range(len(number)-1, -1, -1):
    if number[i] == '0':
        result += 1
    else:
        break

print(result)
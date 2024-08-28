n, m = map(int, input().split())

k = int(input())

arr = []

for _ in range(k):
    now = list(map(int, input().split()))
    arr.append(now)

dic, loca = map(int, input().split())

result = 0

for item in arr:
    if dic == 2:
        if item[0] == 3:
            result += (loca + (m - item[1]))
        elif item[0] == 4:
            result += ((n-loca) + (m-item[1]))
        elif item[0] == 1:
            result += min((m+loca+item[1]), (m+(n-loca)+(n-item[1])))
        elif item[0] == 2:
            result += abs(loca-item[1])
    elif dic == 1:
        if item[0] == 3:
            result += (loca + item[1])
        elif item[0] == 4:
            result += ((n-loca) + item[1])
        elif item[0] == 1:
            result += abs(loca-item[1])
        elif item[0] == 2:
            result += min((m+loca+item[1]), (m+(n-loca)+(n-item[1])))
    elif dic == 3:
        if item[0] == 3:
            result += abs(loca-item[1])
        elif item[0] == 4:
            result += min((n+loca+item[1]), (n+(m-loca)+(m-item[1])))
        elif item[0] == 1:
            result += (loca + item[1])
        elif item[0] == 2:
            result += ((m-loca) + item[1])
    elif dic == 4:
        if item[0] == 3:
            result += min((n + loca + item[1]), (n + (m-loca) + (m-item[1])))
        elif item[0] == 4:
            result += abs(loca-item[1])
        elif item[0] == 1:
            result += (loca + (n-item[1]))
        elif item[0] == 2:
            result += ((m-loca) + (n-item[1]))
print(result)

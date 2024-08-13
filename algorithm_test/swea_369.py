n = int(input())
result = []

for i in range(1, n+1):
    if '3' not in str(i) and '6' not in str(i) and '9' not in str(i):
        result.append(i)
    else:
        cnt_3 = str(i).count('3')
        cnt_6 = str(i).count('6')
        cnt_9 = str(i).count('9')
        result.append("-" * (cnt_3 + cnt_6 + cnt_9))
print(*result)
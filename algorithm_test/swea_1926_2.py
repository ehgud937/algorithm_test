N = int(input())
arr = list(range(1, N+1))

result = ''

for i in arr:
    cnt = 0
    if '3' in str(i) or '6' in str(i) or '9' in str(i) :
        cnt += str(i).count('3')
        cnt += str(i).count('6')
        cnt += str(i).count('9')
        result += '-'*(cnt) + ' '
    else:
        result += str(i) + ' '

print(result)
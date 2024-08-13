t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_min = 999999
    idx = 0
    for i in range(n):
        person1 = 0
        person2 = 0
        person1 += sum(arr[:i+1])
        person2 += sum(arr[i+1:])
        if abs(person1 - person2) < sum_min:
            sum_min = abs(person1 - person2)
            idx = i + 1
    print(f'#{tc} {idx} {sum_min}')
        
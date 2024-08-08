switch = int(input())
switch_list = list(map(int, input().split()))
people = int(input())

for _ in range(people):
    sex, number = map(int, input().split())
    if sex == 1:
        for idx, current in enumerate(switch_list):
            if (idx+1) % number == 0:
                switch_list[idx] = 1 - current
    else:
        n = 1
        while True:
            if number-1-n < 0 or number-1+n >= switch:
                switch_list[number-1] = 1 - switch_list[number-1]
                break
            if switch_list[number-1-n] != switch_list[number-1+n]:
                switch_list[number-1] = 1 - switch_list[number-1]
                break
            else:
                switch_list[number-1-n] = 1 - switch_list[number-1-n]
                switch_list[number-1+n] = 1 - switch_list[number-1+n]
                n += 1
                
for i in range(0, len(switch_list), 10):
    print(*switch_list[i : i+10])
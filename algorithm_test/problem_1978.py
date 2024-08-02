t = int(input())

my_list = list(map(int, input().split()))
num = 0


for i in range(t):
    if my_list[i] != 1:
        prime = 0
        for j in range(1, 100):
            if j != 1 and j != my_list[i]:
                if my_list[i] % j == 0:
                    prime += 1
        if prime == 0:
            num +=1
print(num)
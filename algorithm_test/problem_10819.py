from itertools import permutations

n = int(input())
num_arr = list(map(int, input().split()))

per_arr = list(permutations(num_arr))

max_num = 0
for new_arr in per_arr:
    now_sum = 0
    for i in range(len(new_arr)-1):
        now_sum = now_sum + abs(new_arr[i] - new_arr[i+1])
    if now_sum > max_num:
        max_num = now_sum
print(max_num)
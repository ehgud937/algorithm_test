# import sys

# up, down, high = map(int, sys.stdin.readline().split())

# now = 0
# n = 0
# while now < high:
#     n += 1
#     now += up
#     if now >= high:
#         break
#     now -= down

# print(n)

import sys

up, down, high = map(int, sys.stdin.readline().split())

if up >= high:
    print(1)
elif (high - up) % (up - down) == 0:
    print((high - up) // (up - down) + 1)
elif (high-up) <= (up - down):
    print(2)
else:
    print(high// (up-down) + 1)
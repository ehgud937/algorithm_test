import sys
input = sys.stdin.readline

def is_palindrome(s):
    return s == s[::-1]

def my_func(s):
    left, light = 0, len(s)-1
    
    while left < light:
        if s[left] != s[light]:
            s1 = s[:left] + s[left+1:]
            s2 = s[:light] + s[light+1:]

            if is_palindrome(s1) or is_palindrome(s2):
                return 1
            else:
                return 2
        left += 1
        light -= 1
    return 0

t = int(input())

for _ in range(t):
    s = input().strip()

    print(my_func(s))
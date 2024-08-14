def is_falindrome(s):
    if s == s[::-1]:
        return len(s)

for _ in range(1, 11):
    tc = int(input())

    arr = [list(input()) for _ in range(1)]
    max_cnt = 0
    for row in arr:
        if row == row[::-1]:
            if max_cnt < len(row):
                max_cnt = len(row)
                break
        else:
            left = 0
            right = len(row) - 1
            while left < right:
                s1 = row[left:]
                s2 = row[:right]
                
                if s1 == s1[::-1]:
                    if max_cnt < len(s1):
                        max_cnt = len(s1)
                        break
                else:
                    if s2 == s2[::-1]:
                        if max_cnt < len(s2):
                            max_cnt = len(s2)
                            break
                left += 1
                right -= 1
    print(max_cnt)

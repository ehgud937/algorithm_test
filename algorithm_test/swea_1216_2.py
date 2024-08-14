for _ in range(1, 11):
    tc = int(input())

    arr = [list(input()) for _ in range(100)]

    max_cnt = 0

    for row in arr:
        for i in range(100):
            for j in range(99, i, -1):
                string = row[i : j]
                if string == string[::-1]:
                    if len(string) > max_cnt:
                        max_cnt = len(string)
    for row in list(zip(*arr)):
        for i in range(100):
            for j in range(99, i, -1):
                string = row[i : j]
                if string == string[::-1]:
                    if len(string) > max_cnt:
                        max_cnt = len(string)
    print(f'{tc} {max_cnt}')
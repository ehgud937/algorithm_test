ratio = {(2, 1, 1): 0,
         (2, 2, 1) : 1,
         (1, 2, 2) : 2,
         (4, 1, 1) : 3,
         (1, 3, 2) : 4,
         (2, 3, 1) : 5,
         (1, 1, 4) : 6,
         (3, 1, 2) : 7,
         (2, 1, 3) : 8,
         (1, 1, 2) : 9}

t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    arr = list(set([input() for _ in range(n)]))
    answer = 0
    temp = []
    for i in arr:
        password = format(int(i, 16), 'b').lstrip('0')
        ratio_1 = 0
        ratio_2 = 0
        ratio_3 = 0
        cnt = 0
        even = 0
        odd = 0
        mola = ''
        for j in password:
            if j == '1' and ratio_2 == 0:
                ratio_1 += 1
            elif j == '0' and ratio_1 != 0 and ratio_3 == 0:
                ratio_2 += 1
            elif j == '1' and ratio_2 != 0:
                ratio_3 += 1
            elif ratio_3 != 0:
                cnt += 1
                k = min(ratio_1, ratio_2, ratio_3)
                num = ratio[(ratio_1//k,  ratio_2//k, ratio_3//k)]
                mola += str(num)
                ratio_3, ratio_2, ratio_1 = 0, 0, 0
                if cnt == 8:
                    if (odd*3 + even + num) % 10 == 0 and mola not in temp:
                        answer += odd+even+num
                    temp.append(mola)
                    even = 0
                    odd = 0
                    cnt = 0
                    mola = ''
                elif cnt % 2 == 0 :
                    even += num
                else:
                    odd += num
    print(f'#{tc} {answer}')
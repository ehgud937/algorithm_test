h2b = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}
dic = {'0001101' : 0,
       '0011001' : 1,
       '0010011' : 2,
       '0111101' : 3,
       '0100011' : 4,
       '0110001' : 5,
       '0101111' : 6,
       '0111011' : 7,
       '0110111' : 8,
       '0001011' : 9}

hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

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
    final = 0
    for i in arr:
        password = format(int(i, 16), 'b').lstrip('0')
        ratio_1 = 0
        ratio_2 = 0
        ratio_3 = 0
        odd = 0
        even = 0
        cnt = 0
        result = ''
        for num in password:
            if num == '1' and ratio_2 == 0:
                ratio_1 += 1
            elif num == '0' and ratio_1 != 0 and ratio_3 == 0:
                ratio_2 += 1
            elif num == '1' and ratio_2 != 0:
                ratio_3 += 1
            elif ratio_3 != 0:
                cnt += 1
                k = min(ratio_1, ratio_2, ratio_3)
                mola = ratio[(ratio_1//k, ratio_2//k, ratio_3//k)]
                result += str(mola)
                ratio_3, ratio_2, ratio_1 = 0, 0, 0
                if cnt == 8:
                    # for i in range(len(result)):
                    #     if i % 2 == 0:
                    #         odd += int(result[i])
                    #     else:
                    #         even += int(result[i])
                    if ((odd * 3) + even) % 10 == 0 and result not in temp:
                        final += even + odd

                    temp.append(result)
                    odd = 0
                    even = 0
                    result = ''
                elif cnt % 2 == 0:
                    odd += mola
                else:
                    even += mola
    print(f'#{tc} {final}')
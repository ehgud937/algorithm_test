n = int(input())

size_list = list(map(int, input().split()))

t, p = map(int, input().split())

t_cnt, pen_cnt, spen_cnt = 0, 0, 0

for shirt in size_list:
    if shirt != 0 :    
        if shirt <= t:
            t_cnt += 1
        elif shirt % t == 0:
            t_cnt += (shirt//t)
        else:
            t_cnt += (shirt//t + 1)

pen_cnt, spen_cnt = n//p, n%p

print(t_cnt)
print(pen_cnt, spen_cnt , end=' ')



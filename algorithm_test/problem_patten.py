p = 'tta'
t = 'tttttabcttata'
n = len(t)
m = len(p)
cnt = 0

for i in range(n-m+1):  # 비교 시작 위치
    for j in range(m):
        if t[i + j] != p[j]:
            break       # for j, 다음 글자부터 비교 시작
    else:         # for j가 중단없이 반복되면
        cnt += 1        #패턴 개수 1증가
print(cnt)
t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    cheak_list1 = []
    cheak_list2 = []
    cheak_list3 = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    # 가로 점검
    for i in range(len(arr)):
        cheak_list = []
        for j in range(len(arr)):
            cheak_list.append(arr[i][j])
        cheak_list1.append(cheak_list)
    
    for i in cheak_list1:
        if len(set(i)) == 9:
            cnt1 += 1
    
    # 세로 점검
    for i in range(len(arr)):
        cheak_list = []
        for j in range(len(arr)):
            cheak_list.append(arr[j][i])
        cheak_list2.append(cheak_list)
    
    for i in cheak_list2:
        if len(set(i)) == 9:
            cnt2 += 1
    
    # 3x3 점검
    for i in range(0, len(arr), 3):
        for j in range(0, len(arr), 3):
            cheak_list = []
            cheak_list.append(arr[i][j])
            cheak_list.append(arr[i][j+1])
            cheak_list.append(arr[i][j+2])
            cheak_list.append(arr[i+1][j])
            cheak_list.append(arr[i+1][j+1])
            cheak_list.append(arr[i+1][j+2])
            cheak_list.append(arr[i+2][j])
            cheak_list.append(arr[i+2][j+1])
            cheak_list.append(arr[i+2][j+2])
            
            cheak_list3.append(cheak_list)
    
    for i in cheak_list3:
        if len(set(i)) == 9:
            cnt3 += 1
    
    
    # 최종 스도쿠 확인
    if cnt1 and cnt2 and cnt3 == 9:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
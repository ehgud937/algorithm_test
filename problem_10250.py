T = int(input())
for i in range(T):
    rooms = []
    H, W, N = map(int, input().split())
    for w in range(1, W+1):
        for h in range(1, H+1):
            if w < 10 :
                rooms.append(str(h)+ '0'+ str(w))
            else :
                rooms.append(str(h) + str(w))
    print(rooms[N-1])
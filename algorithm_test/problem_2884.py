H, M = map(int,input().split())

if M >= 45 :
    print(H, (M - 45))
elif (M < 45 and H >= 1) :
    print((H - 1), 60 - (45 - M))
else :
    print(23, 60 - (45 - M)) 
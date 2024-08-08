import sys
t = int(sys.stdin.readline())

for _ in range(t):
    string = sys.stdin.readline().strip()
    
    if string == string[::-1]:
        print(0)
        continue
    
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            string_1 = string.replace(string[i], '')
            string_2 = string.replace(string[-(i+1)], '')
            if string_1 == string_1[::-1]:
                print(1)
                break
            elif string_2 == string_2[::-1]:
                print(1)
                break
    else:
        print(2)


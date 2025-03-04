
di = [-1, 0, 1, 0]  
dj = [0, 1, 0, -1]  

def simulate(N, M, r, c, d, room):
    cleaned_count = 0
    cleaned = [[False] * M for _ in range(N)]  
    
    while True:
        if not cleaned[r][c]:  
            cleaned[r][c] = True
            cleaned_count += 1
        
        found = False
        for _ in range(4):  
            d = (d - 1) % 4 
            nr = r + di[d]
            nc = c + dj[d]
            
            if 0 <= nr < N and 0 <= nc < M and not cleaned[nr][nc] and room[nr][nc] == 0:
                r, c = nr, nc  
                found = True
                break
        
        if not found:  
            nr = r - di[d]  
            nc = c - dj[d]
            
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
                r, c = nr, nc  
            else:
                break  
    
    return cleaned_count

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]


print(simulate(N, M, r, c, d, room))
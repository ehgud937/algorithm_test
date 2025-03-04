board = [ list(map(int, input().split())) for _ in range(19) ]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

winner = 0
win_x, win_y = 0, 0

for x in range(19):
    for y in range(19):
        if board[x][y] == 0:
            continue
        
        for i in range(4):
            nx = x
            ny = y
            cnt = 1
            
            px = x - dx[i]
            py = y - dy[i]
            
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
                    break
                if board[nx][ny] != board[x][y]:
                    break
                cnt += 1

            if cnt == 5:
                if 0 <= px < 19 and 0 <= py < 19 and board[px][py] == board[x][y]:
                    continue
                if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y]:
                    continue
                    
                winner = board[x][y]
                win_x = x + 1
                win_y = y + 1

print(winner)
if winner != 0:
    print(win_x, win_y)
import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def add(board, dir):
    N = len(board)
    now_board = [[0] * N for _ in range(N)]

    if dir in ['left', 'right']:
        for i in range(N):
            numbers = [x for x in board[i] if x]

            if dir == 'right':
                numbers.reverse()

            merge = []
            j = 0

            while j < len(numbers):
                if j+1 < len(numbers) and numbers[j] == numbers[j+1]:
                    merge.append(numbers[j] * 2)
                    j += 2
                else:
                    merge.append(numbers[j])
                    j += 1

            if dir == 'right':
                merge.reverse()
                start = N - len(merge)
            else:
                start = 0
            
            for j, num in enumerate(merge):
                now_board[i][j + start] = num

    else:
        for i in range(N):
            numbers = [board[j][i] for j in range(N) if board[j][i]]
            
            if dir == 'down':
                numbers.reverse()

            merge = []
            j = 0

            while j < len(numbers):
                if j+1 < len(numbers) and numbers[j] == numbers[j+1]:
                    merge.append(numbers[j] * 2)
                    j += 2

                else:
                    merge.append(numbers[j])
                    j += 1

            if dir == 'down':
                merge.reverse()
                start = N - len(merge)
            else:
                start = 0

            for j, num in enumerate(merge):
                now_board[start + j][i] = num
    
    return now_board

def find(board, max_cnt):
    if max_cnt == 5:
        return max(max(row) for row in board)
    
    return max(find(add(board, d), max_cnt+1)
        for d in ['left', 'right', 'up', 'down'])

print(find(board, 0))
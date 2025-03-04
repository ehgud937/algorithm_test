import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def move(board, direction):
    N = len(board)
    new_board = [[0] * N for _ in range(N)]
    
    if direction in ['left', 'right']:
        for i in range(N):
            nums = [x for x in board[i] if x]
            if direction == 'right': nums.reverse()
            
            merged = []
            j = 0
            while j < len(nums):
                if j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    merged.append(nums[j] * 2)
                    j += 2
                else:
                    merged.append(nums[j])
                    j += 1
                    
            if direction == 'right':
                merged.reverse()
                start = N - len(merged)
            else:
                start = 0
            for j, num in enumerate(merged):
                new_board[i][start + j] = num
                
    else:
        for j in range(N):
            nums = [board[i][j] for i in range(N) if board[i][j]]
            if direction == 'down': nums.reverse()
            
            merged = []
            i = 0
            while i < len(nums):
                if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    merged.append(nums[i] * 2)
                    i += 2
                else:
                    merged.append(nums[i])
                    i += 1
                    
            if direction == 'down':
                merged.reverse()
                start = N - len(merged)
            else:
                start = 0
            for i, num in enumerate(merged):
                new_board[start + i][j] = num
                
    return new_board

def find_max_value(board, depth=0):
    if depth == 5:
        return max(max(row) for row in board)
    
    return max(find_max_value(move(board, d), depth + 1) 
              for d in ['left', 'right', 'up', 'down'])

print(find_max_value(board))
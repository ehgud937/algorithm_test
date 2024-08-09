def backtrack(row, current_sum):
    global min_sum

    if row == n:    # 모든 행을 다 탐색 현재 합계와 최솟값 비교
        min_sum = min(min_sum, current_sum)
        return

    for col in range(n):    # 열을 하나씩 선택
        if not visited[col]:    # not false == true 방문하지 않았으면
            visited[col] = True # 방문 표시
            print(visited)
            backtrack(row + 1, current_sum + matrix[row][col])  # 다음 행으로 이동과 현재 선택 행 +
            visited[col] = False    # 모든 행을 다 돌았을 때 다시 방문을 위해
            print()
            print(visited)
            print()


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * n
    min_sum = 1000000000

    backtrack(0, 0)

    print(f'#{tc} {min_sum}')
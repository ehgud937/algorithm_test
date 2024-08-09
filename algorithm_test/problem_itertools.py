import itertools

def find_min_sum(matrix, n):
    min_sum = 999

    for col in itertools.permutations(range(n)):
        current_sum = sum(matrix[i][col[i]] for i in range(n))
        min_sum = min(current_sum, min_sum)

    return min_sum

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    result = find_min_sum(matrix, n)

    print(f'#{tc} {result}')

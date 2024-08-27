def inorder(arr, idx, result):
    if idx >= len(arr):
        return result

    inorder(arr, 2*idx+1, result)
    result.append(arr[idx])
    inorder(arr, 2*idx+2, result)

for tc in range(1, 11):
    n = int(input())
    arr = list(range(1, n+1))
    order = {}
    result = []

    for _ in range(n):
        current = list(input().split())
        order[current[0]] = current[1]

    inorder(arr, 0, result)

    answer = '' # 김도형 바보

    for i in result:
        answer += order[str(i)]

    print(f'#{tc} {answer}')
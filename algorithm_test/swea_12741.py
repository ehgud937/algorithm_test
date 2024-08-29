t = int(input())

results = []

for tc in range(1, t+1):
    one_start, one_end, two_start, two_end = map(int, input().split())

    overlap_start = max(one_start, two_start)
    overlap_end = min(one_end, two_end)

    result = max(0, overlap_end - overlap_start)

    results.append(f'#{tc} {result}')


print("\n".join(results))
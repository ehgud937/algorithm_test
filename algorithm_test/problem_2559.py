n, m = map(int, input().split())
arr = list(map(int, input().split()))
current = sum(arr[:m])
max_temperature = current

for i in range(1, n - m + 1):
    current = current - arr[i-1] + arr[i+m-1]
    max_temperature = max(max_temperature, current)

print(max_temperature)
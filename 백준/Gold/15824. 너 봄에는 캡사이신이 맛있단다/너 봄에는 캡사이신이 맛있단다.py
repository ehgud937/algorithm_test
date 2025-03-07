MOD = 10**9 + 7

def calculate_pain_index(N, scovilles):
    scovilles.sort()
    power = [1] * N
    for i in range(1, N):
        power[i] = (power[i-1] * 2) % MOD
    
    total = 0
    for i in range(N):
        max_count = power[i]
        min_count = power[N - i - 1]
        total = (total + scovilles[i] * (max_count - min_count)) % MOD
    
    return total

# 입력 처리
N = int(input())
scovilles = list(map(int, input().split()))
# 결과 출력
print(calculate_pain_index(N, scovilles))

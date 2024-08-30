t = int(input())

for tc in range(1, t+1):
    a_fee, b_fee, b_under, b_fer_fee, use = map(int, input().split())

    a_result = a_fee * use
    b_result = 0
    if use <= b_under:
        b_result = b_fee
    else:
        b_result = b_fee + ((use - b_under) * b_fer_fee)

    print(f'#{tc} {min(a_result, b_result)}')
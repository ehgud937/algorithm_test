def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win(l, r):
    if arr[l] == arr[r]:
        return l
    elif (arr[l] == 1 and arr[r] == 3) or (arr[l] == 2 and arr[r] == 1) or (arr[l] == 3 and arr[r] == 2):
        return l
    else:
        return r

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [0] + list(map(int ,input().split()))
    result = f(1, n)
    print(f'#{tc} {result}')
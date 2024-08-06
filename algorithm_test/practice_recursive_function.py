def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def f(i, n):    # i 현재 인덱스, n 크기
    if i == n:  # 배열을 벗어난 경우
        return
    else:
        print(arr[i])
        f(i+1, n)
        return

# arr = [1, 2, 3]
# n = 3
# f(0, 3)

def vec(i, n, v):
    if arr[i] == v:
        return 1
    elif i == n:
        return 0
    else:
        return vec(i+1, n, v)

arr = [1, 2, 3, 4, 'abc', 5]
n = 6
c = 'abc'

print(vec(0, n, c))
def f(i, n, k, p):
    if i == k:
        print(p[:k])
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            f(i+1, n, k, p)
            p[i], p[j] = p[j], p[i]

arr = [1,2,3,4,5]

f(0, 5, 3, arr)
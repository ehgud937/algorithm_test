import itertools
#
#
# def backtrack(a, k, n):
#     c = [0] * maxcandidates
#
#     if k == n:
#         process_solution(a, k)
#
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k + 1, n)
#
# def construct_candidates(a, k, n, c):
#     c[0] = True
#     c[1] = False
#     return 2
#
# def process_solution(a, k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end = ' ')
#     print()
#
# maxcandidates = 2
# nmax = 4
# a = [0] * nmax
# num = [1, 2, 3, 4]
# backtrack(a, 0, nmax)


# print(list(itertools.permutations([1,2,3,4],2)))
# t = int(input())
#
# for tc in range(1, t+1):
#     n, k = map(int, input().split())
#     arr = list(range(1,12))
#
#     for i in range(1<<12):
#         sum_num = 0
#         cnt = 0
#         for j in range(12):
#             if i & (1<<j):
#                 sum_num += arr[j]
#                 cnt += 1
#         if sum_num == k and cnt == n:
#     print(cnt)
# # ##########
# # arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
# min_num = 0
#
# for row in arr:
#     min_num += min(row)
# print(min_num)

############
# def f(i, k, s, t): # i원소, k 집합의 크기, s i-1까지 고려된 합, t목표
#     global cnt
#     global fcnt
#     fcnt += 1
#     if i == k: # 모든 원소 고려
#         if s == t:
#             cnt += 1
#         return
#     else:
#         bit[i] = 1
#         f(i + 1, k, s + a[i], t)
#         bit[i] = 0
#         f(i + 1, k, s, t)
#
#
#
# a = list(range(1, 11))
# n = 10
#
# key = 55
# cnt = 0
# bit = [0] * n
# fcnt = 0
# f(0, n, 0, key)
# print(cnt)
# print(fcnt)


import itertools


def find_min_sum(matrix, N):
    min_sum = float('inf')

    for perm in itertools.permutations(range(N)):
        current_sum = sum(matrix[i][perm[i]] for i in range(N))
        min_sum = min(min_sum, current_sum)

    return min_sum


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = find_min_sum(matrix, N)

    print(f"#{t} {result}")
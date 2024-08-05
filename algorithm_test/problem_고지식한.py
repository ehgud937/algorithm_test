# def f(t, p):
#     n = len(t)
#     m = len(p)
#
#     for i in range(n - m + 1):
#         for j in range(m):
#             if t[i + j] != p[j]:
#                 break
#         else:
#             return 1
#     return 0
#
# t = int(input())
#
# for tc in range(1, t+1):
#     a = input()
#     b = input()
#     print(f'#{tc}', f(b, a))

t = int(input())


for tc in range(1, t+1):
    text, word = map(str, input().split())
    cnt = 0
    i = 0
    while i <= len(text)-len(word):
        if text[i : i + len(word)] == word:
            cnt += 1
            i += len(word)
        else:
            i += 1

    result = (len(text) - (cnt * len(word))) + cnt
    print(f'#{tc} {result}')
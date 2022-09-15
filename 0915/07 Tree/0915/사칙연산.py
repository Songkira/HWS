import sys; sys.stdin = open('1232.txt', 'r')

for tc in range(1, 10+1):
    N = int(input())
    tree = [0] * (N + 1)
    lst = []

    for _ in range(N):
        arr = list(input().split())

        if len(arr) == 2:
            n, val = int(arr[0]), int(arr[1])
            tree[n] = val
        else:
            lst.append([int(arr[0]), arr[1], int(arr[2]), int(arr[3])])

    for i in range(len(lst)-1, -1, -1):
        n, val, a, b = lst[i]

        if val == '+':
            tree[n] = tree[a] + tree[b]
        elif val == '-':
            tree[n] = tree[a] - tree[b]
        elif val == '*':
            tree[n] = tree[a] * tree[b]
        elif val == '/':
            tree[n] = tree[a] // tree[b]

    print(f'#{tc}', tree[1])


# -------------------------------------------

#         operator = ['+', '-', '*', '/']
#
#
#         def check(v):
#             if arr[v] in operator:
#                 l = check(L[v])
#                 r = check(R[v])
#                 return cal(arr[v], l, r)
#             return arr[v]
#
#
#         def cal(operator, l, r):
#             if operator == '+':
#                 result = l + r
#             elif operator == '-':
#                 result = l - r
#             elif operator == '*':
#                 result = l * r
#             else:
#                 result = l / r
#             return result
#
#
#         for case in range(1, 11):
#             N = int(input())
#             arr = [0] * (N + 1)
#             L = [0] * (N + 1)
#             R = [0] * (N + 1)
#             for _ in range(N):
#                 data = list(input().split())
#                 if len(data) == 2:
#                     v, val = map(int, data)
#                     arr[v] = val
#                 else:
#                     v, val, l, r = int(data[0]), data[1], int(data[2]), int(data[3])
#                     arr[v] = val
#                     L[v] = l
#                     R[v] = r
#             print(f'#{case} {int(check(1))}')
#
# # ------------------------------------------
# for tc in range(1, 11):
#     N = int(input())
#
#     tree = [0] * (N + 1)  # [0, 0, 0, 10, 88, 65]
#     lst = []
#     cal = []
#     for _ in range(N):
#         arr = list(input().split())
#
#         if len(arr) <= 2:
#             tree[int(arr[0])] = int(arr[1])
#         else:
#             cal.append(arr)
#
#     for _ in range(len(cal)):
#         n, caln, a, b = cal.pop()
#         na = tree[int(a)]
#         nb = tree[int(b)]
#
#         if caln == '+':
#             tree[int(n)] = int(na) + int(nb)
#         elif caln == '-':
#             tree[int(n)] = int(na) - int(nb)
#         elif caln == '*':
#             tree[int(n)] = int(na) * int(nb)
#         elif caln == '/':
#             tree[int(n)] = int(na) // int(nb)
#     print(f'#{tc}', tree[1])
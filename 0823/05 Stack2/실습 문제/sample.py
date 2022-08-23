# import sys; sys.stdin = open('4881.txt', 'r')
# arr = [[2, 1, 2],
#        [5, 8, 5],
#        [7, 2, 2]
#        ]
# N = 3
# cols = [i for i in range(N)]
# def perm(k, cur_sum): # cur_sum : 지금까지 선택한 요소들의 합
#     global ans
#     if cur_sum >= ans:
#         return
#     if k == N:
#         if ans > cur_sum:
#             ans = cur_sum
#     else:
#         for i in range(k, N):
#             cols[k], cols[i] = cols[i], cols[k]
#             perm(k + 1, cur_sum + arr[k][cols[k]])   # arr[k][cols[k]]
#             cols[k], cols[i] = cols[i], cols[k]
#
# ans = 999999999999
# perm(0, 0)
# print(ans)


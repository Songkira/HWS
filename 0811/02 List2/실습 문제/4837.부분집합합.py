import sys; sys.stdin = open("4837.txt", "r")

T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)

lst = []
for i in range(1 << n):
    sub_lst = []
    for j in range(n):
        if i & (1 << j):
            sub_lst.append(A[j])
    lst.append(sub_lst)

for tc in range(T):
    N, K = map(int, input().split())

    len_lst= []
    for i in lst:
        if len(i) == N:
            len_lst.append(i)

    cnt = 0
    for i in len_lst:
        if sum(i) == K:
            cnt += 1

    print(f'#{tc+1} {cnt}')

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# N = len(A)
#
# for bits in range(1<<N): # 2^N(3) = 8
#     for i in range(N): # N=3 이므로, i => 0, 1, 2
#         if bits & (1 << i):
#             print(A[i], end=" ")
#     print()

# #------------------------------
# arr = [10, 20, 30]
# bits = [0] * len(arr) # [0, 0, 0]
#
# for i in range(2):
#     bits[0] = i
#     for j in range(2):
#         bits[1] = j
#         for k in range(2):
#             bits[2] = k
#             print(bits, end='')
#             for l in range(3):
#                 if bits[l]: print(arr[l], end='')
#             print()
# # [0, 0, 0]
# # [0, 0, 1]30
# # [0, 1, 0]20
# # [0, 1, 1]2030
# # [1, 0, 0]10
# # [1, 0, 1]1030
# # [1, 1, 0]1020
# # [1, 1, 1]102030

# ----------------------------------
# bit shift 연산자
# val = 10
# << : 2배 증가
# >>: 1/2 로 감소
# print(val << 1) # 20
# print(val << 2) # 40
# print(1 << 2) # 4
# print(10 >> 1) # 5
# print(10 >> 2) # 2 # 원래 2.5인데, 범위를 벗어나면 버려지게 됨.

# print(10 & 2) # 2
# 같은 위치에 있는 애들끼리 and를 함.
# 10 = 1010(2)
#  2 = 0010(2)
# 공통 = 0010(2) -> 2
# -----------------------------------
# val = 10
# for i in range(3, -1, -1):
#     if val & (1 << i):
#         print('1', end=' ')
#     else:
#         print('0', end=' ')
# print()
#----------------------------
# arr = [10, 20, 30]
# N = len(arr)
# #
# for bits in range(1<<N): # 2^N(3) = 8
#     # print(bits) bits 는 2진수로 표현된 하나의 방식. 12345 이런거하고 다를거 없음.
#     # 0 -> 000
#     # 1 -> 001
#     # 2 -> 010
#     # 3 -> 011
#     # 4 -> 100
#     # 5 -> 101
#     # 6 -> 110
#     # 7 -> 111
#     for i in range(N): # N=3 이므로, i => 0, 1, 2
#         if bits & (1 << i):
#             print(arr[i], end=' ')
#     print()
        # 10
        # 20
        # 10 20
        # 30
        # 10 30
        # 20 30
        # 10 20 30
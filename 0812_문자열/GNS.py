import sys; sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())

for tc in range(T):
    lst = list(input().split())
    # test = int(lst[1])
    lst1 = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    lst2 = list(input().split())

    sort_lst = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                sort_lst.append(lst2[j])
    print(f'{lst[0]}', *sort_lst)
#----------------------------------------------------------------
# 교수님

#--------------------------------------------------------------
# 내가 무대뽀로 진행한 코드
#     for i in range(N):
#         if num_lst[i] == 'ZRO':
#             num_lst[i] = 0
#         if num_lst[i] == 'ONE':
#             num_lst[i] = 1
#         if num_lst[i] == 'TWO':
#             num_lst[i] = 2
#         if num_lst[i] == 'THR':
#             num_lst[i] = 3
#         if num_lst[i] == 'FOR':
#             num_lst[i] = 4
#         if num_lst[i] == 'FIV':
#             num_lst[i] = 5
#         if num_lst[i] == 'SIX':
#             num_lst[i] = 6
#         if num_lst[i] == 'SVN':
#             num_lst[i] = 7
#         if num_lst[i] == 'EGT':
#             num_lst[i] = 8
#         if num_lst[i] == 'NIN':
#             num_lst[i] = 9
#
#     for a in range(N-1):
#         min_idx = a
#         for b in range(a+1, N):
#             if num_lst[min_idx] > num_lst[b]:
#                 min_idx = b
#         num_lst[a], num_lst[min_idx] = num_lst[min_idx], num_lst[a]
#
#     for i in range(N):
#         if num_lst[i] == 0:
#             num_lst[i] = 'ZRO'
#         if num_lst[i] == 1:
#             num_lst[i] = 'ONE'
#         if num_lst[i] == 2:
#             num_lst[i] = 'TWO'
#         if num_lst[i] == 3:
#             num_lst[i] = 'THR'
#         if num_lst[i] == 4:
#             num_lst[i] = 'FOR'
#         if num_lst[i] == 5:
#             num_lst[i] = 'FIV'
#         if num_lst[i] == 6:
#             num_lst[i] = 'SIX'
#         if num_lst[i] == 7:
#             num_lst[i] = 'SVN'
#         if num_lst[i] == 8:
#             num_lst[i] = 'EGT'
#         if num_lst[i] == 9:
#             num_lst[i] = 'NIN'
#
#     print(f'{lst[0]}',*num_lst)
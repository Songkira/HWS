import sys; sys.stdin = open("4865.txt", "r")

T = int(input())

# for tc in range(1, T +1):
#     str1 = list(input()) # 찾을 문자열
#     str2 = list(input()) # 비교할 전체 문자열
#     M = len(str1)
#     N = len(str2)

# 가장 많은 글자의 개수를 출력하려면 카운팅?
#     # 카운팅 배열 생성 했는데 str 타입이라 안됨. 수정
#     cnt = [0]*26 # 알파벳 개수가 26개라서
#     for st in str2:
#         cnt[st] += 1 # str 타입이라 안됨. 수정은 어떻게?
#     str_dic1 = {}
#     for alpha in str1:
#         if alpha in str_dic1:
#             str_dic1[alpha] += 1
#         else:
#             str_dic1[alpha] = 1
#     # print(str_dic1)
#
#     str_dic2 = {}
#     for ab in str2:
#         if ab in str_dic2:
#             str_dic2[ab] += 1
#         else:
#             str_dic2[ab] = 1
#     # print(str_dic2)
#     sort_dic1 = sorted(str_dic1.items(), key=lambda x:x[1])
#     sort_dic2 = sorted(str_dic2.items(), key=lambda x:x[1])
#
#     max_idx = 0
#     word = ''
#     cnt = 0
#     for i in range(1, len(sort_dic1)):
#         if sort_dic1[max_idx][1] < sort_dic1[i][1]:
#             max_idx = i
#             word = sort_dic1[max_idx][0]
#         elif sort_dic1[max_idx][1] == sort_dic1[i][1]:
#             for j in range(1, len(sort_dic2)):
#                 if sort_dic2[max_idx][1] < sort_dic2[j][1]:
#                     max_idx = j
#                     cnt = sort_dic2[max_idx][1]
#
#             for w in range(len(str2)):
#                 if str2[w] == word:
#                     cnt += 1

                # #
    # if sort_dic1[max_idx][1] == sort_dic1[i][1]:
    #     for j in range(1, len(sort_dic2)):
    #         if sort_dic2[max_idx][1] < sort_dic2[j][1]:
    #             max_idx = j
    #             cnt = sort_dic2[max_idx][1]
# 삽질한거

# ----------------------------------------------
# str1에서 있는 문자중 str2에 가장 많은 수를 갖고 있는 문자를 찾는거 였음
for tc in range(1, T + 1):
    str1 = set(input())  # 찾을 문자열
    str2 = input()  # 비교할 전체 문자열

    l = len(str2)

    max_cnt = 0
    for al in str1:
        cnt = 0
        for j in range(l):
            if al == str2[j]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')
#
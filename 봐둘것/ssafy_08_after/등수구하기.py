# N = 리스트 점수 갯수, score = 태수의 점수,
# P = 리스트에 올라갈 수 있는 점수의 개수
N, score, P = map(int, input().split())
# 현재 랭킹 리스트에 있는 점수
# rank_lst = list(map(int, input().split()))
# rank_lst.sort(reverse=True)
# rank_lst.insert(0, 0)
# # print(rank_lst)

if N == 0:
    print(1)
else:
    rank_lst = list(map(int, input().split()))
    if N == P and rank_lst[-1] >= score:
        print(-1)
    else:
        rank = N + 1
        for i in range(N):
            if rank_lst[i] <= score:
                rank = i + 1
                break
        print(rank)
# for i in range(1, P+1):
#     if len(rank_lst) == 1:
#         if rank_lst[i-1] <= score:
#             rank_lst.insert(i, score)
#             print(i)
#             break
#     elif len(rank_lst) < P+1:
#         if rank_lst[i] <= score:
#             rank_lst.insert(i, score)
#             print(i)
#             break
#         elif rank_lst[-1] > score:
#             rank_lst.insert(-1, score)
#             print(len(rank_lst)-1)
#             break
#     elif len(rank_lst) == P+1:
#         if rank_lst[i] < score:
#             rank_lst.insert(i, score)
#             rank_lst.pop()
#             print(i)
#             break
#         elif rank_lst[i] == score:
#             print(-1)
#             break

print(rank_lst)

# 리스트 맨앞 인덱스에 데이터 추가하는 방법
# lst = [2, 9, 3]

# 1 / insert('인덱스', '데이터')
# lst.insert(0, 'a')
# print(lst) => ['a', 2, 9, 3]

# 2
# from collections import deque
# deq = deque(lst)
# deq.appendleft('a')
# new_lst = list(deq)
# print(new_lst) -> ['a', 2, 9, 3]



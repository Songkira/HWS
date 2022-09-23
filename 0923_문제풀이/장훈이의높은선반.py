import sys; sys.stdin = open('장훈이의높은선반.txt')
# 부분 집합 생성
# arr = [1, 2, 3, 4]
# N = len(arr)
# pick = []

# # 부분집합 전부 생성
# def backtrack(k, cur_sum):
#     if k == N:
#         if cur_sum >= B:
#             lst.append(cur_sum)
#     else:
#         backtrack(k + 1, cur_sum + H[k])    # k번 원소를 포함
#         backtrack(k + 1, cur_sum)    # k번 원소를 배제
#
# for tc in range(1, int(input())+1):
#     # N = 점원 수, B = 선반의 높이
#     N, B = map(int, input().split())
#     # 각 점원들의 키
#     H = list(map(int, input().split()))
#
#     # 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑
#     lst = []
#     backtrack(0, 0)
#     print(f'#{tc} {min(lst) - B}')

# --------------------------------------------
# # 풀이 / 정현석
# for tc in range(1, int(input())+1):
#     # N = 점원 수, B = 선반의 높이
#     N, B = map(int, input().split())
#     # 각 점원들의 키
#     H = list(map(int, input().split()))
#
#     mnv = 1e9
#     temp = []
#     for i in range(N):
#         temp.append(H[i])
#         if H[i] == B:
#             mnv = H[i]
#             break
#         for j in range(len(temp) - 1):
#             res = H[i] + temp[j]
#             if res == B:
#                 mnv = res
#                 break
#             elif res < B:
#                 temp.append(res)
#             elif B <= res < mnv:
#                 mnv = res
#         if mnv == B:
#             break
#     print(f'#{tc} {mnv - B}')
# # ------------------------------------------------
# # 교수님 풀이, 너비 우선
# from collections import deque
#
# t = int(input())
# for tc in range(t):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     Q = deque()
#     Q.append((0, 0))        # (k, cur_sum)
#
#     ans = 0xffffff
#     while Q:
#         k, cur_sum = Q.popleft()
#         if k == N:
#             # if cur_sum >= B and cur_sum - B < ans:
#             if cur_sum >= B:
#                 print(cur_sum)
#         else:
#             Q.append((k + 1, cur_sum + arr[k]))
#             Q.append((k + 1, cur_sum))

def backtrack(k, cur_sum, remain):
    if cur_sum >= B:
        # 계산하고
        return
    # if cur_sum > B: return
    if cur_sum + remain < B: return

    if k == N:
        return
    else:
        backtrack(k + 1, cur_sum + arr[k], remain - arr[k])
        backtrack(k + 1, arr[k], remain - arr[k])

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    total = sum(arr)
    backtrack(0, 0, total)

# # --------------------------------------------------
# # 풀이 / 가지치기
# def track(depth, tmp):  # tmp: 현재까지의 합
#     global res, max_v
#
#     if depth == n:
#         if tmp >= b:
#             res = min(tmp, res)
#         return
#
#     if tmp > res:
#         return
#
#     if (n-depth) * max_v + tmp < b:
#         return
#
#     track(depth+1, tmp + li[depth])
#     track(depth + 1, tmp)


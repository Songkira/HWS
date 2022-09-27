import sys; sys.stdin = open('백트래킹_전기버스2.txt', 'r')

# # 삽질중...
# def smtime(i, N):
#     global answer
#     global cnt
#     cnt += 1
#     if i == N:
#         s = 0
#         for k in range(1, N+1):
#             if Bus_used[i]:
#                 s += Battery[k]
#         if s == N:
#             answer += 1
#             for n in range(N):
#                 if Bus_used[n]:
#                     print(Battery[i], end=' ')
#             print()
#     else:
#         Bus_used[i] = 1
#         smtime(i+1, N)
#         Bus_used[i] = 0
#         smtime(i + 1, N)
#
# for tc in range(1, int(input())+1):
#     lst = list(map(int, input().split()))
#     N = num =lst[0]                      # 정류장 수
#     # 마지막 정류장에는 배터리가 없음
#     Battery = [0] + lst[1:] + [0]   # 정류장 별 배터리
#     Bus_used = [0] * (N + 1)        # 정류장 이동체크?
#
#
#     # 최소한의 교체 횟수로 목적지에 도착
#     # min_num = 101
#     answer = 0      # 부분집합의 합 == N
#     cnt = 0
#     smtime(0, num)
#     print(answer)

# -----------------------------------------------



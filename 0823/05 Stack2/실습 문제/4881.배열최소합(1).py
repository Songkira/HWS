import sys; sys.stdin = open('4881.txt', 'r')

for tc in range(1, int(input())+1):
    # 합구하기
    # N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # cols = [i for i in range(N)] # [0,1, ....., N-1]
    #
    # def perm(k):
    #     if k == N:
    #         S = 0
    #         for i in range(N):
    #             S += arr[i][cols[i]]
    #         print(cols, S)
    #     else:
    #         for i in range(k, N):
    #             cols[k], cols[i] = cols[i], cols[k]
    #             perm(k+1)
    #             cols[k], cols[i] = cols[i], cols[k]
    # perm(0)
    # [0, 1, 2] 12
    # [0, 2, 1] 9
    # [1, 0, 2] 8
    # [1, 2, 0] 13
    # [2, 1, 0] 17
    # [2, 0, 1] 9
# -----------------------------------------------------
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cols = [i for i in range(N)] # [0,1, ....., N-1]
#
#     def perm(k):
#         if k == N:
#             S = 0
#             for i in range(N):
#                 S += arr[i][cols[i]]
#             print(cols, S)
#             global ans
#             if ans > S: # 합 중 최소값 구하기
#                 ans = S
#         else:
#             for i in range(k, N):
#                 cols[k], cols[i] = cols[i], cols[k]
#                 perm(k+1)
#                 cols[k], cols[i] = cols[i], cols[k]
#
#     ans = 100000000000000000000
#     perm(0)
#     print(ans) # 8
# ---------------------------------------------------
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # cols = 순열을 만들기 위해 인위적으로 만든 배열
#     cols = [i for i in range(N)] # [0,1, ....., N-1]
#
#     def perm(k, cur_sum):
#         if k == N:
#             S = 0
#             for i in range(N):
#                 S += arr[i][cols[i]]
#             print(cols, S, cur_sum) # S 와 cur_sum의 값이 같음
#             global ans
#             if ans > S: # 합 중 최소값 구하기
#                 ans = S
#         else:
#             for i in range(k, N):
#                 cols[k], cols[i] = cols[i], cols[k] # k행의 열의 위치를 선택
#                 perm(k+1, cur_sum + arr[k][cols[k]]) # k번 행의 결정
#                 cols[k], cols[i] = cols[i], cols[k]
#
#     ans = 100000000000000000000
#     perm(0, 0)
#     print(ans)
    # [0, 1, 2] 12 12
    # [0, 2, 1] 9 9
    # [1, 0, 2] 8 8
    # [1, 2, 0] 13 13
    # [2, 1, 0] 17 17
    # [2, 0, 1] 9 9
    # 8
# --------------------------------------------------------------
# 가지치기 = 여기서 끊어야 된다는 근거가  있어야됨.
# Branch and Bound: 분기의 함정

    # N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # # cols = 순열을 만들기 위해 인위적으로 만든 배열
    # cols = [i for i in range(N)] # [0,1, ....., N-1]
    #
    # def perm(k, cur_sum):
    #     global ans
    #     if cur_sum >= ans:
    #         return
    #
    #     if k == N:
    #         S = 0
    #         for i in range(N):
    #             S += arr[i][cols[i]]
    #         print(cols, S, cur_sum) # S 와 cur_sum의 값이 같음
    #         if ans > S: # 합 중 최소값 구하기
    #             ans = S
    #     else:
    #         for i in range(k, N):
    #             cols[k], cols[i] = cols[i], cols[k] # k행의 열의 위치를 선택
    #             perm(k+1, cur_sum + arr[k][cols[k]]) # k번 행의 결정
    #             cols[k], cols[i] = cols[i], cols[k]
    #
    # ans = 100000000000000000000
    # perm(0, 0)
    # # print(ans)
    # # [0, 1, 2] 12 12
    # # [0, 2, 1] 9 9
    # # [1, 0, 2] 8 8

# ------------------------------------------------------
# 부분집합 합 구할때도 가지치기 part 있음.

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # cols = 순열을 만들기 위해 인위적으로 만든 배열
    cols = [i for i in range(N)]  # [0,1, ....., N-1]

    def perm(k, cur_sum):
        global ans
        if cur_sum >= ans:
            return

        if k == N:
            if ans > cur_sum:  # 합 중 최소값 구하기
                ans = cur_sum
        else:
            for i in range(k, N):
                cols[k], cols[i] = cols[i], cols[k]  # k행의 열의 위치를 선택
                perm(k + 1, cur_sum + arr[k][cols[k]])  # k번 행의 결정
                cols[k], cols[i] = cols[i], cols[k]


    ans = 100000000000000000000
    perm(0, 0)
    print(ans)
    # [0, 1, 2] 12 12
    # [0, 2, 1] 9 9
    # [1, 0, 2] 8 8
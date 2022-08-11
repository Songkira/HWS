import sys; sys.stdin = open('4835.txt')

# T = int(input())
#
# for tc in range(T):
#     l, n = map(int, input().split())
#     nums = list(map(int, input().split()))
#     lst = []
#     for i in range(n, l+1):
#         total = 0
#         for j in range(i-n, i):
#             total += nums[j]
#         lst.append(total)
#     max = lst[0]
#     min = lst[0]
#     for k in range(1, len(lst)):
#         if lst[k] > max:
#             max = lst[k]
#         elif lst[k] < min:
#             min = lst[k]
#     print(f'#{tc+1}', max-min)

# ---------------------------------------
# 위 코드 수정.
# T = int(input())
#
# for tc in range(T):
#     l, n = map(int, input().split())
#     nums = list(map(int, input().split()))
#     lst = []
#     max = 0
#     min = 1000000
#     for i in range(n, l+1):
#         total = 0
#         for j in range(i-n, i):
#             total += nums[j]
#         if max < total:
#             max = total
#         elif min > total:
#             min = total
#
#     print(f'#{tc+1}', max-min)
# --------------------------------------------
# 교수님것
T = int(input())

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    S = 0
    # 첫번째 구간의 합
    for i in range(M):
        S += arr[i]
    max_sum = min_sum = S # 첫번째 구간의 합을 기준값(S)으로 잡음

    for e in range(M, N): # 두번째 구간부터 모든 구간의 끝 인덱스
        S = S - arr[e] - arr[e - N]
        if max_sum < S:
            max_sum = S
        if min_sum > S:
            min_sum = S
    print(f'#{T}', max_sum - min_sum)
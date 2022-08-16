import sys; sys.stdin = open('4834.txt')

T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     arr = list(map(int, input()))
#     c = [0] * 10
#     for i in range(N):
#         c[arr[i]] += 1
#         print(arr[i])
#         print(c)
#         max_val = c[0]
#         max_idx = 0
#         for j in range(10): # c 인덱스가 10개
#             if c[j] >= max_val: # 값이 같은 경우
#                 max_val = c[j]
#                 max_idx = j
#     print(f'#{tc + 1} {max_idx} {max_val}')
#----------------------------------------------------
for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))
    c = [0] * 10
    for i in arr:
        c[i] += 1
        max_val = c[0]
        max_idx = 0
        for j in range(10):
            if c[j] >= max_val:
                max_val = c[j]
                max_idx = j
    print(f'#{tc+1} {max_idx} {max_val}')
# T = int(input())
# for test in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     s = 0
#     max_num = 0
#     for i in range(N-1):
#         s = arr[i] + arr[i+1]
#         if max_num < s:
#             max_num = s
#     print(f'#{test+1} {max_num}')
# ==================
# 배열 사용해서 다시 풀어보기

T = int(input())

for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    for i in range(N):
        s = 0
        for j in range(1, N):
            if i == j-1:
                s = arr[i]+arr[j]
            if max_num < s:
                max_num = s

    print(f'#{test + 1} {max_num}')

import sys; sys.stdin = open('4869.txt', 'r')

# def Box(N):
#     if N >= 2:
#         return (Box(N-2)*2)+Box(N-1)
#     else:
#         return 1
#
# for tc in range(1, int(input())+1):
#     N = int(input()) // 10
#     print(Box(N))
#------------------------------------
# T = int(input())
#
# def paper(N):
#     if N % 10 == 0:
#         if N == 10:
#             return 1
#         elif N == 20:
#             return 3
#         else:
#             return paper(N - 10) + (2 * paper(N - 20))
#
# #
# for t in range(T):
#     N = int(input())
#     count = paper(N)
#     print(f"#{t + 1}", count)
#     # A가 n개,n-1개,n-2개 일때
#     # B가 n개일때
#     # 너비는 N*20 <- 수식에 필요한가?



def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return count(n-1) + count(n-2)*2

for tc in range(1, int(input())+1):
    N = int(input())//10
    print(f'#{tc}', count(N))

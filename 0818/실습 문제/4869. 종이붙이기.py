import sys; sys.stdin = open('4869.txt', 'r')

def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return count(n - 1) + count(n - 2) * 2


for tc in range(1, int(input()) + 1):
    N = int(input()) // 10
    print(f'#{tc}', count(N))

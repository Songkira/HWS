import sys; sys.stdin = open('1486.txt')

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    R = sum(H) - B
    def subset(k, i, j):
        global ans
        if i >= B:
            ans = min(ans, i - B)
            return
        if j > R: return
        if k == N:
            return

        subset(k + 1, i + H[k], j)
        subset(k + 1, i, j + H[k])

    ans = 0xfffff
    subset(0, 0, 0)
    print('#{} {}'.format(tc, ans))
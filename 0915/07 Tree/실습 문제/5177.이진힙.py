import sys; sys.stdin = open('5177.txt', 'r')
#=================================================


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    H = [0] * (N + 1)
    idx = 0
    for val in arr:
        idx += 1
        H[idx] = val
        c, p = idx, idx//2
        while p and H[c] < H[p]:
            H[c], H[p] = H[p], H[c]

    ans = 0
    idx = N // 2
    while idx:
        ans += H[idx]
        idx //= 2

    print(ans)
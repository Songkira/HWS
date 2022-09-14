import sys; sys.stdin = open('5178.txt', 'r')
#=================================================

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(N - M, 0, -1):
        tree[i] += tree[i*2]
        if i*2 + 1 <= N:
            tree[i] += tree[i * 2 + 1]

    print(tree[L])


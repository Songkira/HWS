import sys; sys.stdin = open('5176.txt', 'r')
#=================================================

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    cnt = 1
    def inorder(v):
        global cnt
        if v > N: return

        inorder(v << 1)
        tree[v] = cnt
        cnt += 1
        inorder((v << 1) + 1)

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N >> 1]}')
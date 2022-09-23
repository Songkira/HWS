import sys; sys.stdin = open('1486.txt')
from collections import deque

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    Q = deque()
    Q.append((0, sum(arr)))
    ans = 0xfffff
    while Q:
        k, s = Q.popleft()

        if s < ans:  ans = s
        if k == N: continue
        if s - arr[k] >= B:
            Q.append((k + 1, s - arr[k]))
        Q.append((k + 1, s))

    print('#{} {}'.format(tc, ans - B))
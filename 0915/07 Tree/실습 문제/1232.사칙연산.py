import sys; sys.stdin = open('1232.txt', 'r')
#=================================================

for tc in range(1, 11):
    N = int(input())
    L = [0] * (N+1)
    R = [0] * (N + 1)
    D = [0] * (N + 1)

    for _ in range(N):
        arr = input().split()
        idx = int(arr[0])
        val = arr[1]
        if len(arr) == 4:
            D[idx] = val
            L[idx], R[idx] = int(arr[2]), int(arr[3])
        else:
            D[idx] = int(val)

    def calc(v):
        if L[v] == 0:
            return D[v]

        l = calc(L[v])
        r = calc(R[v])

        if D[v] == '+': return l + r
        if D[v] == '-': return l - r
        if D[v] == '*': return l * r
        if D[v] == '/': return l / r

    print(int(calc(1)))
import sys; sys.stdin = open('4835.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_val = 0 # 가장 큰 값을 받기 위해 가장 작은 값인 0으로 설정.
    min_val = 999999 # 가장 작은 값을 받기 위해 미리 큰 수를 설정.

    for s in range(0, N-M +1): # 0 1 2
        e = s + M - 1 # 2 3 4
        val = 0

        for i in range(s, e+1):
            val += arr[i]

        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val

    print(f'#{tc+1} {max_val-min_val}')
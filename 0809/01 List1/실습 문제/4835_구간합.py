import sys; sys.stdin = open('4835.txt')
# 이웃한 M개의 합
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_val = 0 # 가장 큰 값을 받기 위해 가장 작은 값인 0으로 설정.
    min_val = 999999 # 가장 작은 값을 받기 위해 미리 큰 수를 설정.

    # N - M 까지 나와야하는데 경계 에 있으므로 +1을 해서 포함시킨다
    for s in range(0, N-M +1): # 0 1 2 # 시작값
        e = s + M - 1 # 2 3 4 # 종료값 # 0부터니까 -1
        val = 0

        for i in range(s, e+1): # e값도 포함되도록 +1
            val += arr[i]

        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val

    print(f'#{tc+1} {max_val-min_val}')
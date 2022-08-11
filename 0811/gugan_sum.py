import sys; sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0

    for i in range(N):
        for j in range(i+1, N):
            if A[i] + A[j] == K:
                cnt += 1
    print(f'#{tc+1} {cnt}')

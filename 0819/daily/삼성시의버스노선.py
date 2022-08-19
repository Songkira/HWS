import sys; sys.stdin = open('삼성시의버스노선.txt', 'r')

for tc in range(1, int(input())+1):
    stop = [0] * 5001 # 1번 ~ 5000번까지
    N = int(input())

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            stop[i] += 1


    P = int(input())
    for _ in range(P):
        p = int(input())
        print(stop[p], end=' ')
    print()
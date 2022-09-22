import sys; sys.stdin = open('컨테이너.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # 3, 2
    W = list(map(int, input().split())) # N(3)개의 컨테이너의 무게
    T = list(map(int, input().split())) # M(2)개 트럭의 적재용량

    W.sort(reverse=True)
    T.sort(reverse=True)
    # print(W, T)
    # [5, 3, 1] [8, 3]
    # [18, 13, 12, 11, 2] [20, 20, 17, 9, 9, 7, 7, 5, 4, 3]
    # [20, 19, 14, 14, 13, 11, 11, 10, 6, 5] [18, 18, 17, 17, 16, 15, 13, 9, 8, 5, 4, 1]

    # # tidx = T 인덱스 / widx = W 인덱스
    # 잘못 쓴 코드
    # tidx = widx = 0
    # sum_gim = 0
    # while widx <= len(W)-1 or tidx <= len(T)-1: #  while 거짓이 되면 빠져나가니까...
    #     if T[tidx] >= W[widx]:
    #         sum_gim += W[widx]
    #         tidx += 1
    #         widx += 1
    #     elif T[tidx] < W[widx]:
    #         widx += 1
    #
    # print(sum_gim)
    tidx = widx = 0
    sum_gim = 0
    while widx < N and tidx < M: #  while 거짓이 되면 빠져나가니까...
        if W[widx] <= T[tidx]:
            sum_gim += W[widx]
            tidx += 1
            widx += 1
        else:
            widx += 1
    print(f'#{tc} {sum_gim}')

    # sum_gim = 0
    # for i in range(M):
    #     for j in range(N):
    #         if T[i] >= W[j]:
    #             sum_gim += W[j]
    #             del W[j]
    #             break
    #         elif T[i] < W[j]:
    #             continue
    #
    # print(sum_gim)
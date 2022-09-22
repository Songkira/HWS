import sys; sys.stdin = open('화물토크.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #
    # time_lst.sort()
    # # print(time_lst)
    #

    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         if time_lst[i][1] <= time_lst[j][0]:

# ------------------------------------------------
# 교수님 풀이
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # 종료시간 순으로 정렬
    arr.sort(key=lambda x: x[1])
    # print(arr)

    pre_finish = 0
    ans = 0
    for start, finish in arr:
        if pre_finish <= start:
           ans += 1
           pre_finish = finish

    print(f'#{tc} {ans}')
import sys; sys.stdin = open('1210.txt', 'r')

UP, LEFT, RIGHT = 0, 1, 2

for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 ==> 출발점
    r = c = 0
    for i in range(100): # 99번행(마지막)을 조사
        if ladder[99][i] == 2:
            r, c = 99, i
            break

    def dfs(r, c):
        if r == 0:
            return c
        else:
            ladder[r][c] = 0
            ret = 0
            if c > 0 and ladder[r][c - 1]:  # 길이 있다면 좌로 이동
                ret = dfs(r, c - 1)
            elif c + 1 < 100 and ladder[r][c + 1]:  # 길이 있다면 우로 이동
                ret = dfs(r, c + 1)
            else:
                ret = dfs(r - 1, c)

            ladder[r][c] = 1 # 돌아가기 전에 1로 복구
            return ret

    ans = dfs(r, c)

    print(ans)
# 상우하좌

def dfs(r, c):
    global cnt
    cnt += 1
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[r][c] == arr[nr][nc] - 1:
                dfs(nr, nc)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = 0

    lst = []
    cnt = 0
    for r in range(N):
        for c in range(N):
            dfs(r, c)
            lst.append([arr[r][c], cnt])
            cnt = 0
    # print(lst)
    max_num = 0
    for l in range(len(lst)):
        if max_num <= lst[l][1]:
            max_num = lst[l][1]
    # print(max)
    max_lst = []
    for l in range(len(lst)):
        if max_num == lst[l][1]:
            max_lst.append(lst[l])
    # print(max_lst)

    print(f'#{tc}', *min(max_lst))


# --------------------------------------------------------



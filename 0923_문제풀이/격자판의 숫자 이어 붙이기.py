import sys; sys.stdin = open('격자판의 숫자 이어 붙이기.txt')
def plus(i, j, word):
    # if depth == 6:
    if len(word) == 7:
        lst.append(word)
        return
    else:
        for n in range(4):
            nr = i + dr[n]
            nc = j + dc[n]
            if 0 <= nr < 4 and 0 <= nc < 4:
                word += arr[nr][nc]
                plus(nr, nc, word)
                # 조합재귀할땐 빼줘야됨
                word = word[:-1]

for tc in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    start = ''
    lst = []
    for r in range(4):
        for c in range(4):
            start = arr[r][c]
            plus(r, c, start)
            # print(start)
    # print(lst)
    set_lst = set(lst)
    # new_lst = sorted(list(set_lst))
    # print(new_lst)
    print(f'#{tc} {len(set_lst)}')


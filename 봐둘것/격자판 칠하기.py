import sys; sys.stdin=open('격자판 칠하기.txt', 'r')
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def check(even, odd):
    for r in range(R):
        for c in range(C):
            if arr[r][c] == '?': continue
            if (r+c) % 2:
                if arr[r][c] != odd:
                    return False
            else:
                if arr[r][c] != even:
                    return False
    return True

for tc in range(1, int(input())+1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]
    print(arr)
    ret1 = check('#', '.')
    ret2 = check('.', '#')

    ans = 'impossible'
    if ret1 or ret2:
        ans = 'possible'

    # for r in range(R):
    #     for c in range(C):
    #         if arr[r][c] == '#':
    #             for i in range(4):
    #                 nr = r + dr[i]
    #                 nc = c + dc[i]
    #                 if 0 <= nr < R and 0 <= nc < C:
    #                     if arr[nr][nc] == '#':
    #                         ans = 'impossible'
    #                         break
    print(f'#{tc} {ans}')
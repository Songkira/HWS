import sys; sys.stdin = open('상호의 배틀필드.txt', 'r')

for tc in range(1, int(input())+1):
    H, W = map(int, input().split())    # H = 높이, W = 너비
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    str_lst = list(input())
    w_lst = ['<', '>', 'v', '^']

    for r in range(H):
        for c in range(W):
            if arr[r][c] in w_lst:
                tank = [r, c]
                for i in range(N):
                    num = 0
                    if str_lst[i] == 'U':
                        arr[r][c] = '^'
                        if 0 <= r-1 < H and arr[r-1][c] == '.':
                            r = r - 1
                            arr[r][c] = '^'
                            arr[r+1][c] = '.'
                    elif str_lst[i] == 'R':
                        arr[r][c] = '>'
                        if 0 <= c+1 < W and arr[r][c+1] == '.':
                            c = c + 1
                            arr[r][c] = '>'
                            arr[r][c-1] = '.'
                    elif str_lst[i] == 'L':
                        arr[r][c] = '<'
                        if 0 <= c-1 < W and arr[r][c-1] == '.':
                            c = c - 1
                            arr[r][c] = '<'
                            arr[r][c+1] = '.'
                    elif str_lst[i] == 'D':
                        arr[r][c] = 'v'
                        if 0 <= r + 1 < H and arr[r+1][c] == '.':
                            r = r + 1
                            arr[r][c] = 'v'
                            arr[r-1][c] = '.'
                    elif str_lst[i] == 'S':
                        for num in range(1, W+1):
                            if arr[r][c] == '<':
                                if 0 <= c-num < W and arr[r][c-num] == '*':
                                    arr[r][c-num] = '.'
                                    break
                            if arr[r][c] == '>':
                                if 0 <= c + num < W and arr[r][c + num] == '*':
                                    arr[r][c + num] = '.'
                                    break
                            if arr[r][c] == 'v':
                                if 0 <= r + num < H and arr[r+num][c] == '*':
                                    arr[r+num][c] = '.'
                                    break
                            if arr[r][c] == '^':
                                if 0 <= r - num < H and arr[r-num][c] == '*':
                                    arr[r-num][c] = '.'
                                    break

    for line in arr:
        print(*line)
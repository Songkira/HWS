

N = 5
M = 3
arr = [[0] * N for _ in range(N)]

def rect_traverse(r, c, M):
    for i in range(r, r+M):
        for j in range(c, c +M):
            arr[i][j] = 1
    return ret

# def rect_clear(r, c, M): # 지우는거/ 재미로 만듦
#     for i in range(r, r+M):
#         for j in range(c, c +M):
#             arr[i][j] = 0

    ans = 0
    # 모든 사각형의 좌상단 좌표를 생성
    for r in range(N - M +1):
        for c in range(N - M + 1):
            # arr[r][c] = 1
            # 좌상단(r,c), 너비/높이 M
            ret = rect_traverse(r, c, M)
            # rect_clear(r, c, M)
            if ans < ret:
                ans = ret
    print(ans)
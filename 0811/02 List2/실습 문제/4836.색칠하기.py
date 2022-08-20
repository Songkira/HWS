import sys; sys.stdin = open("4836.txt", "r")
T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    cnt = 0
    for i in range(N):
        color = list(map(int, input().split()))
        r1 = color[0]
        c1 = color[1]
        r2 = color[2]
        c2 = color[3]

        for r in range(r1, r2 + 1): # (2, 5)
            for c in range(c1, c2 + 1): # (2, 5)
                arr[r][c] += color[-1]

                if arr[r][c] == 3:
                    cnt += 1


    for line in arr:
        print(*line)

    print(f'#{tc+1} {cnt}')

#----------------------------------------------
# 교수님

# 사각영역의 표현
# N = 10
# arr = [[0] * N for _ in range(N)]

# 1) 두 좌표로 사각영역을 표현
#    - 좌상단 꼭지점(r1,c1), 우하단 꼭지점(r2,c2)
# 사각 영역의 순회
# for r in range(r1, r2 + 1):
#     for c in range(c1, c2 + 1):
#         arr[r][c]

# 2) 좌상단 꼭지점(r1, c1)과 너비(w)와 높이(h)
# for r in range(r1, r1 + h):
#     for c in range(c1, c1 + w):
#         arr[r][c]



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [[0] * 10 for _ in range(10)]
#
#     # 사각영역 색칠하기
#     for _ in range(N):
#         # lst = list(map(int, input().split()))
#         r1, c1, r2, c2, color = map(int, input().split())
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 arr[r][c] += color
#
#     # 겹쳐진 영역은 2으로 저장되어 있을거다...
#     cnt = 0
#     for r in range(10):
#         for c in range(10):
#             if arr[r][c] == 3:
#                 cnt += 1
#
#     print(cnt)

# ===============================
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    cnt = 0
    # 사각영역 색칠하기
    for _ in range(N):
        # lst = list(map(int, input().split()))
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if arr[r][c]:
                    cnt += 1
                arr[r][c] += color

    print(cnt)

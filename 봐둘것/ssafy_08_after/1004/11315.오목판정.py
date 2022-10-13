import sys; sys.stdin = open('11315.txt')

# N = 10
# arr = [[0]* N for _ in range(N)]
#
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]
# r, c =3, 4
#
# arr[r][c] = '*'
# # 원하는 거리(칸수)만큼 가고 싶다.
# k = 4 # 기준점을 포함해서
# for i in range(8):      # 방향
#     for j in range(1, k + 1):   # 거리(칸수)
#         nr = r + dr[i] * j
#         nc = c + dc[i] * j
#         # 범위 체크
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             break
#         arr[nr][nc] = i + 1
#
# for line in arr:
#     print(*line)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    ans = 'NO'
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.':
                continue
            # r, c : 모든 돌의 위치
            # (r, c)를 포함해서 5칸 연속으로 돌이 있는지 체크
            for i in range(8):  # 방향
                for j in range(1, 4+1): # 4칸 전진
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    # 범위체크
                    if nr < 0 or nr >= N or nc< 0 or nc >= N:
                        break
                    if arr[nr][nc] == '.':
                        break
                else:
                    # 오목 완성
                    ans = 'YES'

    print(ans)
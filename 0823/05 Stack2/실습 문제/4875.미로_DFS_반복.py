import sys; sys.stdin = open('4875.txt', 'r')
#1 1
#2 1
#3 0
# 미로
# def delta(r, c):
#     # 상하좌우
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     loc = 0
#     for i in range(100):
#         r += dr[loc]
#         c += dc[loc]
#
#         if 0 < r <= N or 0 < c <= N:
#             if arr[r][c] == 3:
#                 return 1
#                 break
#     else:
#         return 0
for tc in range(1, int(input())+1):
    # 하상우좌
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    top = -1
    # print(arr)
    start = []
    r = c = er = ec =0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
                start.append([r, c])
            elif maze[i][j] == 3:
                er, ec = i, j
    # print(start)
    # 3을 찾을동안 얼마나 돌아다녀야할지 모르기 때문에 while문 필요
    while start:
        for i in range(4): # 델타를 돌려야하기 때문에
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if maze[nr][nc] != 1 or maze[nr][nc] == 0:
                start.append([nr, nc])
                nr, nc = r, c
                break
        else:
            start.pop()

    # if start[top] == [er, ec] :
    #     result = 1
    # elif start[top] == [er, ec] :
    #     result = 0
    print(start[top], [er, ec])
    # print(f'#{tc} {result}')

# -------------------------------------------------
# # 교수님 코드
#     visited = [[0]*N for _ in range(N)] # 지나온 길을 기록할 맵
#     S = []
#     # 시작점을 찾는다
#     r = c = er = ec = 0
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 r, c = i, j
#             elif maze[i][j] == 3:
#                 er, ec = i, j
#
#     # 시작점을 방문하고, 스택에 push
#     S = [(r, c)]
#     visited[r][c] = 0 # 시작점
#
#     # 0, [], None => False / 즉, 이외에는 전부 True 라는 뜻
#     # 모종의 이유로 S 도 빈 스택이 되어버리면 False 가 되면서 반복 종료
#     while S: # 빈 스택이 아닐동안 반복
#         for i in range(4):
#             # (r, c)의 상하좌우 인접한 곳의 좌표를 생성
#             nr, nc = r +dr[i], c + dc[i]
#             if nr < 0 or nr >=N or nc <0 or nc >=N: # 경계체크
#                 continue
#             # 목적지는 3이기 때문에 0으로만 가면 절대로 도착 못함
#             # 길이거나 방문안했으면
#             if maze[nr][nc] != 1 and visited[nr][nc] == 0:
#                 S.append((r, c))
#                 visited[nr][nc] = 1
#                 r, c = nr, nc
#                 break
#         else:
#             r, c = S.pop()
#     print(visited[er][ec])





# A~G -> 0~6
adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6
#-----------------------------------------------

# def dfs(v, N):
#     # 스택 초기화
#     visited = [0] * N   # visited 생성
#     stack = [0] * N     # stack 생성
#     top = -1
#     print(v)
#
#     visited[v] = 1      # 시작점 방문 표시
#     while True:
#         # 어느곳을 방문 안했는지 모르니 순서대로 꺼내보기
#         for w in adjList[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w 가 있으면)
#             if visited[w] == 0:     # [false]로 표시한 분들은 0 대신 false 써도 됨
#                 top += 1            # push(v);
#                 stack[top] = v
#                 v = w                # v <- w; (w에 방문)
#                 print(v)            # 방문
#                 visited[w] = 1      # visited[w] <- true;
#                 break
#         else:                       # w가 없으면
#             if top != -1:           # 스택이 비어있지 않은 경우
#                 v = stack[top]      # pop
#                 top -= 1
#             else:                   # 스택이 비어있으면
#                 break               # while 을 빠져나오게 함.
#
# dfs(0, 7) # 0 1 3 5 4 2 6
# dfs(1, 7) # 1 0 2 4 5 3 6

# 모두 방문하는것을 보장하는것이지 최적 경로를 보장하는건 아닌게맞나요? 네.
# 그래서 전체 리스트 True 때 종료가 아니라 pop으로 stack이 비워질때까지 하는건가 보네요..

#---------------------------------------------------------
def dfs(v, N):
    top = -1
    print(v)

    visited[v] = 1      # 시작점 방문 표시
    while True:
        # 어느곳을 방문 안했는지 모르니 순서대로 꺼내보기
        for w in adjList[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w 가 있으면)
            if visited[w] == 0:     # [false]로 표시한 분들은 0 대신 false 써도 됨
                top += 1            # push(v);
                stack[top] = v
                v = w                # v <- w; (w에 방문)
                print(v)            # 방문
                visited[w] = 1      # visited[w] <- true;
                break
        else:                       # w가 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while 을 빠져나오게 함.
N = 7
visited = [0] * N   # visited 생성 /visited = [1, 1, 1, 1, 1, 1, 1]
stack = [0] * N     # stack생성 / stack = [1, 0, 2, 4, 5, 0, 0]
dfs(1, N)
print()
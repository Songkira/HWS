# 그래프는 실세계를 추상화하기 위한 도구
# Graph = 정점들 집합 + 간선들 집합
# 정점 => 사람, 물건, 개념
# 간선 => 정점들의 관계를 표현

# <연습문제 3 그림 참조>

# 그래프는 간선들 저장
# 나가는 쪽을 먼저 들어오는 쪽을 나중에
# ex.
# [1, 2]
# [1, 3]
# [2, 4]
# .
# .
# [6, 7]

# 정점 수 , 간선 수 필요
# 1번 부터 V까지
# 예제는 0번부터라고 쓰임

import sys; sys.stdin = open('graph_input.txt')
# 깊이 우선 탐색

# V, E  = 정점의 개수, 간선의 개수
V, E = map(int, input().split())
# 정점 번호는 1번 ~ V 번까지 사용
# 정점 수만큼 빈 '인접' 리스트를 생성
G = [[] for _ in range(V + 1)]

#------------------------------------
# for i in range(1, V+1):
#     print(i, '-->', G[i])
#     # 1 --> []
#     # 2 --> []
#     # 3 --> []
#     # 4 --> []
#     # 5 --> []
#     # 6 --> []
#     # 7 --> []
#------------------------------------

# # 무향그래프 기준(화살표 방향이 없는)
# for _ in range(E):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)
#
# for i in range(1, V+1):
#     print(i, '-->', G[i])
#     # 1 --> [2, 3]
#     # 2 --> [1, 4, 5]
#     # 3 --> [1, 7]
#     # 4 --> [2, 6]
#     # 5 --> [2, 6]
#     # 6 --> [4, 5, 7]
#     # 7 --> [6, 3]
#
# # 유향그래프 때는
# # G[u].append(v) 하나만
#------------------------------------

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# 정점들의 방문정보를 저장할 공간이 필요
visited = [0] * (V+1)

# 재귀 써서 작성
# 매개변수는 매번 생기는거/ 실행될때마다 새로운 데이터
def dfs(v): # v: 현재 방문할 정점 번호
    # 정점을 방문한다.
    visited[v] = 1; print(v, end=' ')
    # v 의 방문하지 않은 정점들을 조사한다.
    for w in G[v]:
        if visited[w] == 0:
            dfs(w)
    # print(w, end='')

dfs(1) # 시작점을 인자로 함수 호출












# V, E  = 정점의 개수, 간선의 개수
V, E = map(int, input().split())
# 정점 번호는 1번 ~ V 번까지 사용
# 정점 수만큼 빈 '인접' 리스트를 생성
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
# 정점들의 방문정보를 저장할 공간이 필요
visited = [0] * (V+1)

v = 1           # 시작점
visited[v] = 1  # 시작점을 방문하고 스택에 push
S = [v]         # 빈 스택이 아니어야 True 이기때문에 하나를 넣어둠

# 빈 스택이 아니면 True
while S:        # 빈 스택이 아닐동안 반복
    # v의 방문하지 않은 인접 정점 w를 선택
    for w in G[v]:
        if not visited[w]:
        # (v --> w)
        S.append(v)     # 지나온 정점 스택에 v를 기록
        visited[w] = 1
        v = w
        break   # break 안걸면 인접 정점을 모두다 방문해버림
    else:       # for 문이 돌동안 break 안걸림 -> 더이상 v가 갈 곳이 없음
        v = S.pop()     # 이전에 방문한 정점으로 돌아감

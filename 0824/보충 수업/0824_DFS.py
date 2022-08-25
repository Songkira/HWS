# 인접행렬
# name = ['B', 'A', 'C', 'D', 'E']
# arr=[
#     [0,0,0,1,0],
#     [1,0,0,0,0],
#     [1,0,0,0,1],
#     [0,0,0,0,0],
#     [1,1,0,0,0],
# ]

# ----------------------------------
# # DFS 트리 탐색 순서 출력하기
# # 단방향

# name=list(input().split())  # A B C E D F
# arr=[
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
#
# # DFS : A B D E C F
# # BFS : A B C D E F
#
# answer=[]
# def dfs(now):
#      global answer
#      answer.append(name[now])
#
#      for i in range(6):
#           if arr[now][i]==1:
#                dfs(i)
#
#
# dfs(0)  # 탐색을 시작하는 'A' 0번 인덱스
# print(*answer) # A B D E C F

# # -----------------------------------------
# # 그래프(트리모양이 아닌) DFS (깊이우선)으로 탐색하며 탐색하는 순서 출력하기
# 트리모양이 아니면 사이클(양방향 화살표때문에 무한반복)발생 가능.
# 사이클 방지를 위해 표시할 지도 필요.

# 도착지에 도착하는지 안하는지 1번만 확인 가능.

# name=list(input().split())  # A B C D
# arr=[
#     [0,1,1,0],
#     [0,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
# used=[0]*len(name) # 다닌 곳 1로 표시할 배열
# answer=[]
# def dfs(now):
#     global answer
#     answer.append(name[now])
#     for i in range(4):
#         if arr[now][i]==1 :
#             if used[i]==0:
#                 used[i]=1
#                 dfs(i)
#
# used[0]=1
# dfs(0) # A 부터 깊이우선 탐색 시작
# print(*answer)
# # -------------------------------------------------------------
#
# # # 그래프 경로탐색!! (한 정점에서 다른 정점까지 갈 수 있는 방법이 몇가지 있는가?
# name=list(input().split())  # A B C D
# arr=[
#     [0,1,1,0],
#     [0,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
# used=[0]*4
# cnt=0
# 1.
# def dfs(now):
#     global cnt
#     if now==3:
#         cnt+=1
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             dfs(i)
#             used[i]=0
# ---------------------------------------------
# 2.
# def dfs(now):
#     global cnt
#     if name[now]=='D':
#         cnt+=1
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             dfs(i)
#             used[i]=0
#
# # 'A' -> 'D' 경로탐색
# used[0]=1   # 탐색 시작하는 인덱스에 1 체크하고 DFS 시작
# dfs(0)      # 탐색을 시작하는 'A' 0번 인덱스
# print(cnt)
# --------------------------------------------------
# # 최소비용
name=list(input().split())  # A B C D
arr=[
    [0,3,9,0],
    [0,0,1,7],
    [0,1,0,2],
    [0,0,0,0],
]
# #
# # 매개변수 sum일때
# # return 했을때 알아서 그 전 값으로 다시 원상복구됨.
# used = [0] * 4
# Min = int(21e8)
#
# def dfs(now, sum):
#     global Min
#     if name[now] == 'D':
#         # 최소 sum값 구하기
#         if Min > sum:
#             Min = sum
#
#         for i in range(4):
#             if arr[now][i] > 0:
#                 if used[i] == 0:
#                     used[i]=1
#                     dfs(i, sum + arr[now][i])
#                     used[i]=0
# #
# # 'A' -> 'D' 경로탐색 최소비용
# used[0]=1   # 탐색 시작하는 인덱스에 1 체크하고 DFS 시작
# dfs(0, 0)      # 탐색을 시작하는 'A' 0번 인덱스
# print(Min) # 값이 이상하게 나옴 뭐지??

# # 전역변수 sum 일때
# # 들어갈때 내가 앞으로 들어가는 비용을 더하고 들어갔을경우
# # 다시 return 되고나서 더했던 걸 빼줘야함.
#
# used=[0]*4
# Min = int(21e8)
# sum = 0
# def dfs(now):
#     global Min,sum
#     if name[now] == 'D':
#         if Min > sum:
#             Min = sum
#     for i in range(4):
#         if arr[now][i]>0 and used[i]==0:
#             used[i] = 1
#             sum+= arr[now][i]
#             dfs(i)
#             sum += arr[now][i]
#             used[i]=0
#
# # 'A' -> 'D' 경로탐색
# used[0]=1   # 탐색 시작하는 인덱스에 1 체크하고 DFS 시작
# dfs(0)      # 탐색을 시작하는 'A' 0번 인덱스
# print(Min) # 6 # 이건 제대로 나온다.

# # ----------------------------------------------------
#
# # 출발점을 입력 받습니다.
# # 입력받은 출발점 알파벳 부터  E 가 써있는곳 까지 갈 수 있는 방법이
# # 몇가지 있는지 출력해 주세요.
# # A 입력시 3가지
# # D 입력시 1가지
# # B 입력시 3가지

name=['A','B','C','D','E']
st=input()
arr=[
    [0,1,0,0,0],
    [0,0,1,1,1],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [0,0,0,0,0],
]
used=[0]*5
cnt=0
def dfs(now):
    global cnt
    if name[now]=='E':
        cnt+=1
    for i in range(5):
        if arr[now][i]==1 and used[i]==0:
            used[i]=1
            dfs(i)
            used[i]=0

st_index=0
for i in range(5):
    if name[i]==st:
        st_index=i
        break
used[st_index]=1
dfs(st_index)
print(cnt)
# # ---------------------------------------------
# # 출발점을 입력 받은 후
# # E 까지 가는데 드는
# # 최소비용 출력하기!!!
# #
# name=['A','B','C','D','E']
# st=input()  # 출발점 입력
# arr=[
#     [0,4,0,0,0],
#     [0,0,1,2,9],
#     [5,0,0,7,0],
#     [0,0,0,0,1],
#     [0,0,0,0,0],
# ]
# used=[0]*5
#
# Min=int(21e8)
# def dfs(now,sum):
#     global Min
#     if name[now]=='E':
#         # 최소 비용 (최소 sum)
#         if sum<Min:
#             Min=sum
#
#     for i in range(5):
#         if arr[now][i]>0:
#             if used[i]==0:
#                 used[i]=1
#                 dfs(i,sum+arr[now][i])
#                 used[i]=0
#
# # 출발점의 인덱스 확인
# st_index=0
# for i in range(5):
#     if name[i]==st:
#         st_index=i
#         break
#
# used[st_index]=1
# dfs(st_index,0)
# print(Min)
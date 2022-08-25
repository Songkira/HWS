N = 5
visited = [0] * N

# def dfs(i):
#     if i == N:
#         print(visited)
#         return
#     visited[i] = i +1
#     dfs(i+1)
#
# dfs(0)
# print(visited)
# # [1, 2, 3, 4, 5]
# # [1, 2, 3, 4, 5]
#==============================

# def dfs(i):
#     if i == N:
#         print(visited)
#         return
#     visited[i] = i +1
#     dfs(i+1)
#     visited[i] = 0
#
# dfs(0)
# print(visited)
# # [1, 2, 3, 4, 5]
# # [0, 0, 0, 0, 0]
# # 순서대로 했다가 역순으로 빼는거

#==============================

# def dfs(i):
#     if i == N:
#         print(visited)
#         return 0
#
#     visited[i] = i +1
#     ret = dfs(i +1)
#     visited[i] = 0
#     return ret + 1
#
# print(dfs(0))
# print(visited)
# # [1, 2, 3, 4, 5]
# # 5
# # [0, 0, 0, 0, 0]

# ========================
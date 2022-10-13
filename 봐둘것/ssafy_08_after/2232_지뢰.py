
N = int(input())
arr = [0]
for _ in range(N):
    i = int(input())
    arr.append(i)
arr.append(0)
# 연쇄폭탄
# 오르막, 내리막, 언덕
lst = []
for i in range(1, N+1):
    if arr[i-1] <= arr[i] and arr[i] >= arr[i+1]:
        lst.append(i)

for i in lst:
    print(i)
# print(lst)

# # print(arr)
# bomb_l = bomb_r = 0
# lst = []
# for i in range(1, N):
#     for j in range(i+1, N-1):
#         if arr[i] < arr[j]:
#             bomb_l = arr[j]
#             if bomb_l >= arr[i + 1]:
#                 lst.append(i)
    # if arr[i] > arr[i+1]:
    #     if bomb_l >= arr[i+1]:
    #         bomb_l = arr[i+1]
    # # bomb_l = bomb_r = arr[i]
    # if arr[i - 1] < arr[i]:
    #     continue
    # if arr[i-1] > arr[i]:
    #     lst.append(i-1)
    # if arr[i] > arr[i + 1]:
    #     # bomb_r = arr[i + 1]
    #     continue
    # if arr[i] <= arr[i + 1]:
    #     lst.append(i+1)

print(lst)
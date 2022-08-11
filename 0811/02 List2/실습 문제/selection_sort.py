arr = [64, 25, 10, 22, 11]
N = len(arr)
min_idx = 0
for i in range(1, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
print(min_idx) # arr[2] = 10
arr[min_idx], arr[0] = arr[0], arr[min_idx]

print(arr)
min_idx = 0
for i in range(N):
    if arr[min_idx] > arr[i]:
        min_idx = i
print(min_idx)
arr[min_idx], arr[0] = arr[0], arr[min_idx]

# min_idx = 1
# for i in range(2, N):
#     if arr[min_idx] > arr[i]:
#         min_idx = i
# print(min_idx)
# arr[min_idx], arr[1] = arr[1], arr[min_idx]
#
# min_idx = 2
# for i in range(3, N):
#     if arr[min_idx] > arr[i]:
#         min_idx = i
# print(min_idx) # arr[2] = 1
# arr[min_idx], arr[2] = arr[2], arr[min_idx]

#-====================
for j in range(0, N-2+1): # j: 범위 인덱스
    min_idx = j
    for i in range(j +1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
    arr[min_idx], arr[j] = arr[j], arr[min_idx]

print(arr)
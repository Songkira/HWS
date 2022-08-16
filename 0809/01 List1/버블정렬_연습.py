
# 시간복잡도 :  O(n^2)
arr = [55, 7, 78, 12, 42]

for i in range(len(arr), 0, -1):
    for j in range(1, i):
        if arr[j - 1]> arr[j]:
            arr[j -1],arr[j] = arr[j], arr[j - 1]

print(arr)

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
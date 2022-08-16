
arr = [55, 7, 78, 12, 42]
N = len(arr)

# N - 1 ~ 1 까지

for j in range(0, N - 1):
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

for j in range(0, N - 2):
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

for j in range(0, N - 3):
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

for j in range(0, 1):
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
#오름차순
for i in range(N - 1, 0, -1): # n-1 부터 1까지
    for j in range(0, i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
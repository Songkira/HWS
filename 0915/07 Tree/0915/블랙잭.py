
N, M = map(int, input().split())
arr = list(map(int, input().split()))

max = 0
for i in range(N-3+1):
    for j in range(i+1, N-2+1):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] <= M:
                if max < arr[i]+arr[j]+arr[k]:
                    max = arr[i]+arr[j]+arr[k]
print(max)

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

# 모든 부분 집합을 만들어야 할 때
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):      # j번 비트가 0이 아니면 arr[j] 부분집합의 원소
            print(arr[j], end=' ')
    print()

#
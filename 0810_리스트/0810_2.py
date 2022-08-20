# 선택 정렬
arr = [7, 2, 5, 3, 4, 6]
N = len(arr)

for i in range(N-1): # N-2까지
    minidx = i # 구간의 맨 앞을 최소값으로 가정
    for j in range(i+1, N): # 실제 최소값 인덱스 찾기
        if arr[minidx] > arr[j]:
            minidx = j
    arr[minidx],arr[i] = arr[i], arr[minidx] # 최소값을 구간 맨 앞으로

print(arr)
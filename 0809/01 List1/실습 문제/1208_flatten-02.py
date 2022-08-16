import sys; sys.stdin = open('1208.txt')

T = 10

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = max_idx = 0
    max_val = 0
    min_val = 99999

    for i in range(N): # 덤프 횟수 만큼
        for j in range(len(arr)): # arr 길이만큼 반복
            if arr[min_idx] > arr[j]: # arr[1] = 68 > arr[2] = 35
                min_idx = j           # min_idx(1) = j(2) -> min_idx(2)
            if arr[max_idx] < arr[j]: # arr[0] = 42 < arr[1] = 68
                max_idx = j           # max_idx(0) = j(1) -> max_idx(1)

        arr[max_idx] -= 1
        arr[min_idx] += 1

    for i in arr: # 평탄화 작업 후 최대값/최소값 구하기
        if max_val < i: # 제일 많은 상자를 가진 부분
            max_val = i
        if min_val > i: # 제일 적은 상자를 가진 부분
            min_val = i
    print(f'#{tc+1} {max_val-min_val}')

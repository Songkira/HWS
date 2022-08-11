import sys; sys.stdin = open('1208.txt')

T = 10

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = max_idx = 0
    max_val = 0
    min_val = 99999

    for i in range(len(arr)):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] < arr[i]:
            max_idx = i
        if max_val < arr[i]:
            max_val = arr[i]
        if min_val > arr[i]:
            min_val = arr[i]
    # print(max_idx, min_idx, max_val, min_val) # 37 3 100 1
            for num in range(N):
                if max_val == arr[max_idx]:
                    arr[max_idx] -= 1
                if min_val == arr[min_idx]:
                    arr[min_idx] += 1
                N -= 1
            if N == 0:
                print(f'#{tc+1} {max_val-min_val}')


    #
    #     if max_val == arr[i]:
    #         arr[i] -= 1
    #     if min_val == arr[i]:
    #         arr[i] += 1

    # print(arr)
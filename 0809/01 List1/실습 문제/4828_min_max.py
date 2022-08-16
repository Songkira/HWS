import sys; sys.stdin = open('4828.txt')

T = int(input())


for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_idx = min_idx = 0

    for j in range(1, N):
        if arr[max_idx] < arr[j]:
            max_idx = j
        if arr[min_idx] > arr[j]:
            min_idx = j
    print(f'#{i+1}', arr[max_idx]- arr[min_idx])
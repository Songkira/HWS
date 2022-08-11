import sys; sys.stdin = open("4843.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N):
        if i % 2 == 0:
            max_idx = i
            for j in range(i+1, N):
                if lst[max_idx] < lst[j]:
                    max_idx = j
                lst[i], lst[max_idx] = lst[max_idx], lst[i]
        else:
            min_idx = i
            for j in range(i+1, N):
                if lst[min_idx] > lst[j]:
                    min_idx = j
                lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print(lst)
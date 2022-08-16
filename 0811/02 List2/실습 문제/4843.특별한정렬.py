import sys; sys.stdin = open("4843.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    # 홀수번째와 짝수번째를 나눠서 코드 작성
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

#-----------------------------------------------------------

for tc in range(1, int(input)+1):
    N = int(input())
    arr = lst(map(int, input().split()))

    # # 선택정렬
    # # 비교할때는 N-2 까지 남겨놔야 한다,.
    # for i in range(10): # (0, N - 1) # for i in range(0, N-2 +1): # (0, N - 1) # 범위 시작/ 반복횟수와 관련됨
    #     idx = i
    #     if 1 % 2 == 0:
    #         for j in range(i + 1, N):
    #             if arr[idx] < arr[j]:
    #                 idx = j
    #     else:
    #         for j in range(i + 1, N):
    #             if arr[idx] < arr[j]:
    #                 idx = j
    #     arr[i], arr[idx] = arr[idx], arr[i] # arr[0], arr[idx] = arr[idx], arr[0]

    # 마지막 줄 못적음
    # arr.sort()
    # for i in range(5):
    #     print(arr[N -1 -i], arr[i], end ='')
import sys; sys.stdin = open('view.txt', 'r')

for tc in range(10):
    # 하나의 테스트 케이스
    N = int(input()) # 자료수
    arr = list(map(int, input().split()))

    # 나의 아이디어를 코딩
    cnt = 0

    for i in range(2, N - 2):
        max = arr[i - 2]
        if max < arr[i - 1]:
            max = arr[i - 1]
        if max < arr[i + 1]:
            max = arr[i + 1]
        if max < arr[i + 2]:
            max = arr[i + 2]

        if arr[i] > max:
            cnt = cnt + (arr[i] - max)

    print(f'#{tc + 1} {cnt}')

# 교수님-------------------------------------
for tc in range(1, 11):
    N = int(input()) # 자료수
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N - 3 + 1):
        # i 가 기준
        # max_val = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        # ----------------------------------------------------
        max_val = arr[i-2]
        if max_val < arr[i-1]:
            max_val = arr[i-1]
        if max_val < arr[i+1]:
            max_val = arr[i+1]
        if max_val < arr[i+2]:
            max_val = arr[i+2]
        # i 가 클 경우에만 누적.
        if arr[i] > max_val:
            cnt = arr[i] - max_val
        # -------------------------------------------------
        # max_ val = arr[i-2]
        # for val in [arr[i+1], arr[i-1], arr[i+2]]:
        #     if max_val < val:
        #         max_val = val

        # if arr[i] > max_val:
        #     cnt = arr[i] - max_val

    print(cnt)
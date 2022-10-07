import sys; sys.stdin=open('농작물 수확하기.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    sumV = 0
    start = N // 2  # 2
    end = (N // 2) + 1  # 3
    for i in range(end):
        for j in range(start, end):
            sumV += arr[i][j]
        start -= 1
        end += 1

    start = 1
    end = N-1
    for i in range((N//2)+1, N):
        for j in range(start, end):
            sumV += arr[i][j]
        start += 1
        end -= 1

    print(f'#{tc} {sumV}')
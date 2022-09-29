import sys; sys.stdin = open('2일차 - Sum.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += arr[i][j]
            if maxV < sumV:
                maxV = sumV

    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += arr[j][i]
            if maxV < sumV:
                maxV = sumV

    sumV = 0
    for i in range(100):
        sumV += arr[i][i]
        if maxV < sumV:
            maxV = sumV

    sumV = 0
    for i in range(100):
        sumV += arr[i][99-i]
        if maxV < sumV:
            maxV = sumV

    print(f'#{N} {maxV}')
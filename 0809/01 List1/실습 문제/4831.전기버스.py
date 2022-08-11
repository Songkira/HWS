import sys; sys.stdin = open('4831.txt')
T= int(input())

for test in range(T):
    K, N, M = list(map(int, input().split())) # 3 10 5
    arr = list(map(int, input().split())) # 1 3 5 7 9
    start = 0
    cnt = 0
    # 종점까지는 어떻게?
    for i in range(M):

        if start + K >= arr[i]:
            start = arr[i]
            cnt += 1
        elif start + K < arr[i]: # else:
            start = start
            cnt = 0

    if start + K >= N:
        cnt -= 1

    print(f'#{test+1} {cnt}')














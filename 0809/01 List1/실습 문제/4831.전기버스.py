import sys; sys.stdin = open('4831.txt')

T= int(input()) # 3

for test in range(T):
    K, N, M = list(map(int, input().split())) # 3 10 5
    arr = list(map(int, input().split())) # 1 3 5 7 9
    location = 0
    cnt = 0
    # 종점까지는 어떻게?
    for i in range(M):
                                #
        if location + K >= arr[i]: # 나올때마다 체크됨. 어떻게 체크를 빼야 되는가
            location = arr[i]
            cnt += 1
            if arr[-1] - arr[i] < K:
                cnt -= 1
            # if  K > arr[i]: # arr[i]== 정류소 위치가 K 보다 작은게 있으면 cnt -= 1
            #     cnt -= 1
            #     if arr[-2] + K >= N: # 그리고 arr[-2] + K 가 N과 같거나 클때
            #         cnt -= 1         # 마지막 정류소를 체크할지 말지 결정
        elif location + K < arr[i]: # else:
            cnt = 0

    print(f'#{test+1} {cnt}')
















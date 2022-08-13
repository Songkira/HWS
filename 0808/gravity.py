import sys; sys.stdin=open('input (2).txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    # 가로가 100이 아니라 n인 조건
    # 가장 큰 낙차를 구하는 거니까
    # 일단 큰거나 같은값 나오면? 일단 낙차가 -1 되고, 위치 차이값 구하기?
    max = 0
    for i in range(n):
        cnt = 0
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                cnt += 1
        if max < cnt:
            max = cnt
    print(f'#{tc+1} {max}')

        # if arr[max_idx] < arr[i]:
        #     max_idx = i


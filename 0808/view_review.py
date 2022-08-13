import sys; sys.stdin=open('input (3).txt', 'r')

for tc in range(10):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0 # i가 돌때마다 조망권 있는 세대를 더할 변수 설정

    # 왼쪽 끝과 오른쪽 끝은 [0, 0, .... ,0 ,0] 이렇게 구성되어 있으므로
    for i in range(2, n-2):
        max = arr[i-1] # 주위 4곳 [i+1][i+2][i-2][i-1] 중 하나를 기준으로 잡고
        if max < arr[i-2]: # 차례로 비교하여 제일 높은 곳 max로 설정
            max = arr[i-2]
        if max < arr[i+1]:
            max = arr[i+1]
        if max < arr[i+2]:
            max = arr[i+2]

        if arr[i] > max: # 중간 위치인 [i] 보다 max가 작으면
            # 조망권 조건에 부합하는 세대를 더한다.
            cnt = cnt + (arr[i]-max)
        # 중간위치 [i] 보다 max가 더 크면 조망권 조건 부합이 되지 않는다.

    print(f'#{tc+1} {cnt}')

import sys; sys.stdin = open('파리퇴치.txt', 'r')

for tc in range(1, int(input())+1):
    N, S = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max = 0 # 제일 큰 수를 비교할 기준
    for i in range(N-S+1): # 작은 사각형이 이동할 기준을 잡는 행
        for j in range(N-S+1): # 작은 사각형이 이동할 기준을 잡는 열
            sum = 0 # 작은 사각형의 합을 만드는 변수
            for r in range(S): # 작은 사각형을 만들 제한 범위 행
                for c in range(S): # 작은 사각형을 만들 제한 범위 열
                    # 큰 사각형 안에서 작은 사각형이 위치를 이동하면서 더함
                    sum += arr[r+i][c+j] 
            if max < sum: # 사각형의 합(sum)이 max보다 크면  
                max = sum # max는 사각형의 합(sum)으로 바뀐다.

    print(f'#{tc}', max) # 제일 큰 사각형의 합 출력
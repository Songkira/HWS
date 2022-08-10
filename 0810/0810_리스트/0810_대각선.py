N = int(input()) # 줄/행
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
# 전체를 훑어가면서 하는 방식
# 대각선 왼쪽부터 오른쪽 아래로
for i in range(N):
    for j in range(N):
        if i==j:
            s += arr[i][j]

# 1차원으로 하는 방식 # i, j위치가 동일한 부분 때만
s = 0
for i in range(N):
    s +=[i][i]

# 대각선 오른쪽부터 왼쪽아래로
s = 0
for i in range(N):
    s += arr[i][N-1-i]

# 왼쪽,오른쪽 겹치는 부분/ 대각선의 합?
# N // 2 가 좌표

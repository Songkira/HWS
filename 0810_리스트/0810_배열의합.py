N = int(input()) # 줄/행
# 아래 이차원 배열에 있는 원소의 총합을 구할수 있는가?
arr = [list(map(int, input().split()))]

s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]

print(s)
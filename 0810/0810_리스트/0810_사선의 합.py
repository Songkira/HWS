'''
3
1 2 3
4 5 6
7 8 9
'''
N = int(input()) # 줄/행
arr = [list(map(int, input().split())) for _ in range(N)]

# 같은 사선상의 있는 원소들의 합을 구해보고, 그 중 최대값을 구해보시오.
s = [0]*(2*N-1)

for i in range(N):
    for j in range(N):
        s[i+j] += arr[i][j]

print(s)
# [1, 6, 15, 14, 9]
# 1, 2+4, 3+5+7, 6+8, 9
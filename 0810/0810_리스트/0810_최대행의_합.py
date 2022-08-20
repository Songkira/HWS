'''3
각 행의 합을 구하고 그 중 최대 값을 출력하시오...
1 2 3
4 5 6
7 8 9
'''
N = int(input()) # 줄/행
arr = [list(map(int, input().split())) for _ in range(N)]

# 특별한 언급이 없으면 양수/ 음수가 있다면-> 예를들어, 절대값이 10억이라면 그거 곱하기 원소의 수만큼 '되어야' 함?

maxV = 0 # 최대 행의합 최초 기준
for i in range(N):
    rs = 0 # 행의 합
    for j in range(N):# i행의 j열에 접근 필요
        rs += arr[i][j]
    if maxV < rs :
        maxV = rs
print(maxV) # 행의 순서를 바꿔도 결과는 동일.

import sys; sys.stdin = open('백트래킹_최소 생산 비용.txt', 'r')

def nQueen(row, num):
    global min_num

    if row == N:
        if min_num > num:
            min_num = num
            return min_num
    else:                   # row(행)이 N과 같지 않은데
        if min_num < num:   # 이미 min_num보다 num이 클 경우 리턴
            return

        for col in range(N):  # 이번 col 을 열값으로 선택
            if visit[col]: continue  # 같은행, 같은 열은 제외

            visit[col] = 1
            nQueen(row + 1, num + arr[row][col])
            visit[col] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 9999
    visit = [0] * N
    nQueen(0, 0)
    print(f'#{tc} {min_num}')

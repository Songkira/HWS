import sys; sys.stdin = open('1210.txt', 'r')
# 방향 전환
UP, LEFT, RIGHT = 0, 1, 2

for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착점 ==> 출발점
    r = c = 0

    for i in range(100): # 99번(마지막)을 조사
        if ladder[99][i] == 2:
            r, c = 99, i
            break
# 현재 위치에서 이동할 다음 위치를 계산
#  진행중 방향 정보(위,좌,우) 필요
#  교차점을 만나면 좌, 우, 위로 이동하는 방향 결정
# 총 7가지
# 1. 위 => 1.오른쪽, 2. 왼쪽, 3. 위
# 2. 오른쪽 => 1.왼쪽 2.위
# 3. 왼쪽 => 1.오른쪽 2.위
    dir = UP # 위 = 0, 좌=1, 우=2 # UP, LEFT, RIGHT = 0, 1, 2
    while r != 0: #  반복해서 한칸씩 이동
        if dir != RIGHT and c > 0 and ladder[r][c - 1]: # 길이 있다면 좌로이동
            c -= 1
            dir = LEFT
        elif dir !=LEFT and c < 99 and ladder[r][c + 1]: # 길이 있따면 우로 이동
            c += 1
            dir = RIGHT
        else:
            # 위로 이동
            r -= 1
            dir = UP

    print(c)

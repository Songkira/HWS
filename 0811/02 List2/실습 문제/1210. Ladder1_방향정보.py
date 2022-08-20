import sys; sys.stdin = open('1210.txt', 'r')
'''
↑ 
    오른쪽 길이 있으면 오른쪽으로 
    왼쪽 길이 있으면 왼쪽으로 
    위
←
    왼쪽
    위
→
    오른쪽
    위
'''

UP, LEFT, RIGHT = 0, 1, 2

for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 ==> 출발점
    r = c = 0
    for i in range(100): # 99번행(마지막)을 조사
        if ladder[99][i] == 2:
            r, c = 99, i
            break
    dir = UP  # UP=0, LEFT=1, RIGHT=2
    while r: # 반복해서 한칸씩 이동,
        if dir != RIGHT and c > 0 and ladder[r][c - 1]: # 왼쪽 길이 있다면
            c -= 1
            dir = LEFT
        elif dir != LEFT and c < 99 and ladder[r][c + 1]: # 오른쪽 길이 있다면
            c += 1
            dir = RIGHT
        else:
            # 위로 이동
            r -= 1
            dir = UP

    print(c)
import sys; sys.stdin = open('스도쿠 검증.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    sdoku_r = []
    sdoku_r = []
    for i in range(9):
        for j in range(9):

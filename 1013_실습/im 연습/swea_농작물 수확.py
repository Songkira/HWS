import sys; sys.stdin = open('농작물 수확.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sumin = kira = hyounsuk = 0
    for i in range(N-1):
        for j in range(i+1, N):
            pass
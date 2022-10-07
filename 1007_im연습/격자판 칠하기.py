import sys; sys.stdin=open('격자판 칠하기.txt', 'r')

def chess():

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M):

import sys; sys.stdin = open('전기카트.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    # for
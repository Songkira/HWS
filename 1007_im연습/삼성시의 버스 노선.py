import sys; sys.stdin=open('삼성시의 버스 노선.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    A1, B1 = map(int, input().split())
    A2, B2 = map(int, input().split())
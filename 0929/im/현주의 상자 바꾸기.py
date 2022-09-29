import sys; sys.stdin=open('현주의 상자 바꾸기.txt', 'r')

for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())

    box = [0] * (N + 1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for a in range(L, R+1):
            box[a] = i

    print(f'#{tc}', *box[1:])
import sys; sys.stdin = open('숫자 배열 회전.txt','r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]


    new_90 = []
    new_180 = []
    new_270 = []
    word = ''
    for i in range(N):
        for j in range(N-1,-1,-1):
            word += arr[j][i]
            if len(word) == N:
                new_90.append(word)
                word = ''
    # print(new_90)
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            word += arr[i][j]
            if len(word) == N:
                new_180.append(word)
                word = ''
    # print(new_180)
    for i in range(N-1,-1,-1):
        for j in range(N):
            word += arr[j][i]
            if len(word) == N:
                new_270.append(word)
                word = ''
    # print(new_270)

    new = []
    new.append(new_90)
    new.append(new_180)
    new.append(new_270)
    # print(new)

    print(f'#{tc}')
    for i in range(N):
        for j in range(3):
            print(new[j][i], end= ' ')
        print()

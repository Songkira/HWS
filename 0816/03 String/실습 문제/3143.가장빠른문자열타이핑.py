import sys; sys.stdin = open('3143.txt', 'r')

T = int(input())

for tc in range(T):
    A, B = input().split()

    # 단축단어가 여러번 있으면 다 빼야함.
    # 시작과 끝 인덱스 설정해서 구간 길이 만큼
    cnt = 0
    for i in range(0, len(A)-len(B)): # 0, 1, 2
        for j in range(len(A)-len(B), i+len(B)):
            if


    # if B1 in A1:
    #     num = len(A1) - len(B1)

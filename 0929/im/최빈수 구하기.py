import sys; sys.stdin = open('최빈수 구하기.txt', 'r')

for tc in range(1, int(input())+1):
    t = int(input())
    score = list(map(int, input().split()))

    score_lst = [0] * (100+1)
    maxV = 0
    for i in score:
        score_lst[i] += 1
        if maxV < score_lst[i]:
            maxV = i
    print(score_lst)
    print(maxV)

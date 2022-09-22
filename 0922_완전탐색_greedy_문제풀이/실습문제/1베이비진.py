import sys; sys.stdin = open('베이비진.txt')
# 완전탐색
# 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet

def babyjin1(M):
    global tri, runn
    # if n >= m:
    for i in range(M - 2):
        for j in range(i + 1, M - 1):
            for k in range(j + 1, M):
                if card_one[i] == card_one[j] and card_one[j] == card_one[k]:
                    tri += 1
                if card_one[i] + 1 == card_one[j] and card_one[j] + 1 == card_one[k]:
                    runn += 1
    if tri >= 1 or runn >= 1:
        return 1
    elif tri == 0 and runn == 0:
        return 0

def babyjin2(M):
    global tri, runn
    # if n >= m:
    for i in range(M - 2):
        for j in range(i + 1, M - 1):
            for k in range(j + 1, M):
                if card_two[i] == card_two[j] and card_two[j] == card_two[k]:
                    tri += 1
                if card_two[i] + 1 == card_two[j] and card_two[j] + 1 == card_two[k]:
                    runn += 1
    if tri >= 1 or runn >= 1:
        return 1
    elif tri == 0 and runn == 0:
        return 0

for tc in range(1, int(input())+1):
    lst = list(map(int, input().split()))
    N = len(lst)

    card_one = []
    card_two = []
    tri = runn = 0
    for i in range(N):
        if i % 2 == 0:
            card_one.append(lst[i])
            card_one=sorted(card_one)
            if len(card_one) >= 3:
                ans1 = babyjin1(len(card_one))
                if ans1:
                    print(f'#{tc} 1')
                    break
            # break
        else:
            card_two.append(lst[i])
            card_two=sorted(card_two)
            if len(card_two) >= 3:
                ans2 = babyjin2(len(card_two))
                if ans2:
                    print(f'#{tc} 2')
                    break
                # else:
                #     print(f'#{tc} 0')
            # break

    if ans1 == 0 and ans2 == 0:
        print(f'#{tc} 0')

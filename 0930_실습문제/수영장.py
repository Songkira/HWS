import sys; sys.stdin = open('수영장.txt', 'r')

def money_make(month, money):
    global min_money
    if month >= 13:
        min_money = min(min_money, money)
    else:
        money_make(month + 1, money + month_lst[month] * D)
        money_make(month + 1, money + M)
        money_make(month + 3, money + thr_M)

for tc in range(1, int(input())+1):
    D, M, thr_M, Y = map(int, input().split())
    month_lst = [0] + list(map(int, input().split()))

    min_money = Y
    money_make(1, 0)
    print(f'#{tc} {min_money}')

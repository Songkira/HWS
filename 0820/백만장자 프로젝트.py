import sys; sys.stdin = open('input.txt','r')

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 가격이 제일 높을때 팔아야됨.

    val = lst[N-1]
    profit = 0
    # for i in range(1, N):
    #     jim = 0
    #     if lst[max_idx] < lst[i]:
    #         price += lst[max_idx]
    #         max_idx = i
    #         cnt += 1
    #     jim = (lst[max_idx] * cnt) - price
    #     else:
    #         max_idx += i

# ----------------------------------------
    for i in range(N-2, -1, -1):
        # 현재 가격이 저장된 판매 가격보다 크면 판매 가격 변경
        if lst[i] > val:
            val = lst[i]
        # 현재 가격이 저장된 판매 가격보다 작으면 저장된 판매 가격으로 판매
        else:
            profit += val-lst[i]
    print(f'#{tc} {profit}')

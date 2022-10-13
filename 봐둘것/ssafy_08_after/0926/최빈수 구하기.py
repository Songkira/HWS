# import sys; sys.stdin=open('최빈수 구하기.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = [0] * (100 + 1)

    for val in lst:
        cnt[val] += 1
    MaxV = max(cnt)

    MaxV_lst = []
    for i in range(101):
        if MaxV == cnt[i]:
            MaxV_lst.append(i)

    print(f'#{tc} {MaxV_lst[-1]}')
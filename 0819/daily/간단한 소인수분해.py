import sys; sys.stdin = open('간단한 소인수분해.txt', 'r')
# 간단한 소인수분해

for tc in range(1, int(input())+1):
    N = int(input())

    cnt_2 = cnt_3 = cnt_5 = cnt_7 = cnt_11 = 0
    while N >= 1:
        for i in range(20):
            if N % 2 == 0:
                cnt_2 += 1
                N = N//2
            if N % 3 == 0:
                cnt_3 += 1
                N = N // 3
            if N % 5 == 0:
                cnt_5 += 1
                N = N // 5
            if N % 7 == 0:
                cnt_7 += 1
                N = N // 7
            if N % 11 == 0:
                cnt_11 += 1
                N = N // 11
        break
    print(f'#{tc} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}')

#------------------------------------------------------
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    ans = list()
    cnt = 0
    lst = [2, 3, 5, 7, 11]
    for i in lst:
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        ans.append(cnt)

    print(f'#{tc} {ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]}')

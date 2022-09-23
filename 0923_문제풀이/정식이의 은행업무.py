import sys; sys.stdin = open('정식이의 은행업무.txt')


# for tc in range(1, int(input())+1):
    # Two = list(map(int, input()))
    # Thr = list(map(int, input()))
    # Two.reverse()
    # Thr.reverse()
    # two_lst = [0, 1]
    # thr_lst = [0, 1, 2]
    #
    # # idx = 0
    # # for i in range(len(two_lst)):
    # #     if Two[idx] != two_lst[i]:
    # #         Two[idx] = two_lst[i]
    # #     two_num = 0
    # #     for n in range(len(Two)):
    # #         two_num += Two[n] * (2**n)
    # #         print(two_num)
    #
    # Two2 = []
    # Two_sum = []
    # for i in range(len(Two)):
    #     for j in range(len(two_lst)):
    #         if Two[i] != two_lst[j]:
    #             Two2 = Two[:]
    #             Two2[i] = two_lst[j]
    #             two_num = 0
    #             for n in range(len(Two2)):
    #                 two_num += Two2[n] * (2 ** n)
    #             Two_sum.append(two_num)
    #             # print(two_num)
    # Thr2 = []
    # Thr_sum = []
    # for i in range(len(Thr)):
    #     for j in range(len(thr_lst)):
    #         if Thr[i] != thr_lst[j]:
    #             Thr2 = Thr[:]
    #             Thr2[i] = thr_lst[j]
    #             thr_num = 0
    #             for n in range(len(Thr2)):
    #                 thr_num += Thr2[n] * (3 ** n)
    #             Thr_sum.append(thr_num)
    # # print(Thr_sum)
    # for i in range(len(Two_sum)):
    #     for j in range(len(Thr_sum)):
    #         if Two_sum[i] == Thr_sum[j]:
    #             print(f'#{tc} {Two_sum[i]}')

# ---------------------------------------------------
# 교수님 풀이

diff = set()
for i in range(40):
    diff.add(3**i)
    diff.add(2*(3**i))

for tc in range(1, int(input())+1):
    num2 = input()
    N = len(num2)
    num2 = int(num2, 2)     # 10 진수로 저장(메모리에는 2진수로 저장)
    num3 = int(input(), 3)  # 그냥 10 진수로 저장

    for i in range(N):
        # 원하는 위치의 비트를 토글링?
        # 비트 연산자?
        val = num2 ^ (1 << i)
        if abs(num3 - val) in diff:
            ans = val
            break

    print(f'#{tc} {ans}')

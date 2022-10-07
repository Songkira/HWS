import sys; sys.stdin = open('새샘이의 7-3-5 게임.txt', 'r')

for tc in range(1, int(input())+1):
    lst = list(map(int, input().split()))
    n = len(lst)
    # print(lst)

    sumlst = []
    for i in range(n-2):
        sumi = 0
        sumi += lst[i]
        for j in range(i+1, n-1):
            sumj = 0
            sumj += lst[j]
            for k in range(j+1, n):
                sumk = 0
                sumk += lst[k]
                sumlst.append(sumi+sumj+sumk)
    set_lst = list(set(sumlst))
    sort_lst = sorted(set_lst)

    # print(sort_lst)
    print(f'#{tc} {sort_lst[-5]}')
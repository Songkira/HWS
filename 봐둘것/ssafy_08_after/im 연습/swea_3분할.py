
for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))

    MinV = 999999
    sumi = 0
    for i in range(N-2):
        sumi += lst[i]
        sumj = 0
        for j in range(i+1, N-1):
            sumj += lst[j]
            sumk = 0
            for k in range(j+1, N):
                sumk += lst[k]
            sumV = max(sumi, sumj, sumk) - min(sumi, sumj, sumk)
            if MinV > sumV:
                MinV = sumV
    print(f'#{tc} {MinV}')

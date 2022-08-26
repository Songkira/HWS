import sys; sys.stdin = open('원재의 메모리 복구하기.txt', 'r')

for tc in range(1, int(input())+1):
    bits = list(map(int, input()))
    L = len(bits)
    basic = [0] * L

    cnt = 0
    for i in range(L):
        if bits == basic:
            break
        if bits[i] == 1:
            if basic[i] == 1:
                pass
            else:
                cnt += 1
                for j in range(L-1,i,-1):
                    basic[j] = 1
        elif bits[i] == 0:
            if basic[i] == 0:
                pass
            else:
                cnt += 1
                for j in range(L-1,i,-1):
                    basic[j] = 0

    print(f'#{tc} {cnt}')


        # if bits[i] == '1':
        #     for j in range(i, L):
        #         bits[j+n] = '1'
        #         n += 1
        # if bits[i] == '0':
        #     for j in range(i, L):
        #         bits[j+n] = '0'
        #         n += 1

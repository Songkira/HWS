
T = int(input())

for tc in range(1, T+ 1):
    N, M = map(int, input().split())
    number = [input() for _ in range(N)]
    row = end = 0
    real = []

    pwd = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    #
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if number[i][j] == '1':
                row = i
                end = j
                break
        if end:
            break
    start = end - 56 + 1

    for m in range(start, end, 7):
        real.append(pwd[number[row][m:m + 7]])
    print(real)

    odd = real[0] + real[2] + real[4] + real[6]
    even = real[1] + real[3] + real[5] + real[7]
    #
    ans = odd * 3 + even
    if ans % 10 == 0:
        print(f'#{tc}', odd + even)
    else:
        print(f'#{tc}', 0)
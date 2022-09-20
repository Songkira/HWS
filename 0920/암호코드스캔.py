import sys; sys.stdin = open('암호코드2.txt')
'''
1. 16진수 
2. 가변길이 
3.다수암호
'''
pwd = {'0001101':0, '0011001':1, '0010011':2, '0111101':3,
       '0100011':4, '0110001':5, '0101111':6, '0111011':7,
       '0110111':8, '0001011':9}
bin_dict = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
            '4':'0100', '5':'0101', '6':'0110', '7':'0111',
            '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
            'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    barcode = [list(input()) for _ in range(N)]

    change_lst = []
    change = []
    for i in range(N):
        for j in range(M):
            if barcode[i][j] != '0':
                change.append(barcode[i][j])
            if barcode[i][j] == '0':
                change_lst.append(change)
                change = []

    new_change = []
    for c in change_lst:
        if c not in new_change:
            new_change.append(c)
    print(new_change)
    # ['', '1DB176C588D26EC']
    # ['', '328D1AF6E4C9BB', '196EBC5A316C578']

        # for j in range(0, M, 7):
        #     if barcode[i][j:j+7].count('0') == 7:
        #         continue
        #     elif M % 7 == barcode[i][j:j+7].count('0'):
        #         continue
        #     elif barcode[i][j:j+7].count('0') != 7:
        #         change += ''.join(barcode[i][j:j + 7])
        #     elif M % 7 != barcode[i][j:j+7].count('0'):
        #         change += ''.join(barcode[i][j:j + 7])
        #     elif M % 7 == barcode[i][M-(M % 7):M].count('0'):
        #         continue
        # change_lst.append(change)
    C = len(new_change)

    for i in range(1, C):
        two = []
        for j in new_change[i]:
            two += bin_dict[j]
            for k in range(len(two), -1, -1):
                if two[k] == '1':
                    start = k - 56 + 1
                    two = two[start:k+1]
            print(two)
    # ------------------------------
    #
    # arr = '328D1AF6E4C9BB'
    # bin_str = ''
    # for w in arr:
    #     bin_str += bin_dict[w]
    # print(bin_str) # 00110010100011010001101011110110111001001100100110111011
    # real = []
    # for i in range(0, len(bin_str), 7):
    #     real.append(pwd[bin_str[i:i+7]])
    # print(real) # [1, 4, 4, 6, 8, 2, 2, 7]

    # 01110110110001011101101100010110001000110100100110111011
    # 000111011011000101110110110001011000100011010010011011101100

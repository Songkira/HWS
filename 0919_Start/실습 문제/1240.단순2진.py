import sys; sys.stdin = open('1240.txt', 'r')
P = {
     (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3,
     (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7,
     (2, 1, 3): 8, (1, 1, 2): 9
}

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    line_set = set()

    for _ in range(N):
        t = input().rstrip('0')
        if t:
            line_set.add(t)


    code_set = set()
    for line in line_set:
        # line 을 2진수 문자열로 변환
        i = len(line) - 1
        while i >= 0:
            if line[i] == '1':
                # 0101의 패턴을 8번 반복
                codes = []
                for _ in range(8):
                    c1 = c2 = c3 = c4 = 0
                    while line[i] == '0': i -= 1
                    while line[i] == '1': c4 +=1; i -=1 # 1의 개수 카운팅
                    while line[i] == '0': c3 +=1; i -=1 # 0의 개수 카운팅
                    while line[i] == '1': c2 +=1; i -=1 # 1의 개수 카운팅
                    ratio = min(c2, c3, c4)
                    codes.append(P[(c2//ratio, c3//ratio, c4//ratio)])
                code_set.add(tuple(codes))
            i -= 1
    ans = 0
    for codes in code_set:
        odd = codes[1] + codes[3] + codes[5] + codes[7]
        even = codes[0] + codes[2] + codes[4] + codes[6]
        if (odd*3 + even) % 10 == 0:
            ans += odd + even
    print(ans)


